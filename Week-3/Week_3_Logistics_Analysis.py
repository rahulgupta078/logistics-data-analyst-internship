import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "DataCoSupplyChainDataset.csv"
df = pd.read_csv(DATA_PATH, encoding="latin1", low_memory=False)
for col in ["Days for shipping (real)", "Days for shipment (scheduled)", "Order Item Quantity", "Sales", "Order Item Total", "Order Profit Per Order"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["delay_days"] = df["Days for shipping (real)"] - df["Days for shipment (scheduled)"]
df["is_late"] = (df["Delivery Status"].eq("Late delivery") | df["delay_days"].gt(0)).astype(int)
print("Rows/columns:", df.shape)
print("Exact duplicate rows:", df.duplicated().sum())
print(df[["Days for shipping (real)", "Days for shipment (scheduled)", "delay_days", "Order Item Quantity", "Sales", "Order Profit Per Order"]].describe().round(2))
print(df.groupby("Shipping Mode").agg(records=("Order Id", "count"), avg_actual_days=("Days for shipping (real)", "mean"), late_rate=("is_late", "mean")).round(3))
print(df[["Days for shipping (real)", "Days for shipment (scheduled)", "delay_days", "Order Item Quantity", "Sales", "Order Item Total", "Order Profit Per Order", "Late_delivery_risk"]].corr().round(3))
plt.figure(figsize=(8, 4)); df["Days for shipping (real)"].dropna().hist(bins=12); plt.xlabel("Actual shipping days"); plt.ylabel("Records"); plt.tight_layout(); plt.savefig("shipping_time_distribution.png", dpi=160)
