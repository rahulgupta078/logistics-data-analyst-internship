"""
Week 4: Predictive Modeling and Optimization in Logistics Systems
Dataset: DataCo Smart Supply Chain (CSV)
Target: Days for shipping (real), in days.

Run:
    pip install pandas numpy scikit-learn matplotlib
    python Week_4_Logistics_Modeling.py

Place DataCoSupplyChainDataset.csv in the same directory as this script, or update DATA_PATH.
The script deliberately excludes customer names, email, password, address and other identifiers.
It also excludes post-delivery fields such as Delivery Status, Late_delivery_risk and shipping date
to reduce target leakage. This is an educational forecasting prototype, not a production system.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_PATH = "DataCoSupplyChainDataset.csv"
TARGET = "Days for shipping (real)"
FEATURES = [
    TARGET, "Days for shipment (scheduled)", "Shipping Mode", "order date (DateOrders)",
    "Category Name", "Customer Segment", "Market", "Order Region",
    "Order Item Quantity", "Order Item Product Price", "Order Item Discount Rate"
]

def main():
    df = pd.read_csv(DATA_PATH, encoding="latin1", usecols=FEATURES)
    df["order date (DateOrders)"] = pd.to_datetime(df["order date (DateOrders)"], errors="coerce")
    df = df.dropna(subset=["order date (DateOrders)", TARGET])
    df = df.sort_values("order date (DateOrders)").reset_index(drop=True)

    order_date = df["order date (DateOrders)"]
    df["order_month"] = order_date.dt.month.astype(str)
    df["order_weekday"] = order_date.dt.dayofweek.astype(str)
    df["order_year"] = order_date.dt.year.astype(str)
    df["order_dayofyear"] = order_date.dt.dayofyear

    X = df.drop(columns=[TARGET, "order date (DateOrders)"])
    y = df[TARGET].astype(float)

    # Chronological split: earliest 80% for training, latest 20% for final testing.
    split = int(len(df) * 0.80)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    categorical = [c for c in X.columns if X[c].dtype == "object"]
    numeric = [c for c in X.columns if c not in categorical]
    preprocess = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore", min_frequency=30), categorical),
        ("num", SimpleImputer(strategy="median"), numeric)
    ])

    models = {
        "Median baseline": DummyRegressor(strategy="median"),
        "Ridge regression": Ridge(alpha=2.0),
        "Decision tree (depth 10)": DecisionTreeRegressor(
            max_depth=10, min_samples_leaf=100, random_state=42
        )
    }
    for name, estimator in models.items():
        model = Pipeline([("preprocess", preprocess), ("model", estimator)])
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions) ** 0.5
        r2 = r2_score(y_test, predictions)
        print(f"{name}: MAE={mae:.3f} days | RMSE={rmse:.3f} days | R2={r2:.3f}")

    # Operational diagnostic: define late as actual shipping days > scheduled days.
    # This is a dataset-derived proxy and should be checked against the business SLA.
    df["late_proxy"] = df[TARGET] > df["Days for shipment (scheduled)"]
    print("\\nLate-rate proxy by shipping mode:")
    print((df.groupby("Shipping Mode")["late_proxy"].mean() * 100).round(2).to_string())
    print("\\nOverall late-rate proxy:", round(df["late_proxy"].mean() * 100, 2), "%")

if __name__ == "__main__":
    main()
