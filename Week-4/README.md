# Week 4 — Predictive Modeling and Optimization in Logistics Systems

## Objective
Estimate actual shipping duration from order-time features, evaluate regression models on a chronological holdout, and propose evidence-led operational improvements.

## Files
- `Logistics_Data_Analyst_Week_4_Final_Report.docx` — report with methodology, results, charts, optimization plan, limitations, and conclusion.
- `Week_4_Logistics_Modeling.py` — reproducible Python pipeline.
- `charts/` — generated charts used in the report.

## Dataset and target
- Dataset: DataCo Smart Supply Chain.
- Rows analyzed: 180,519
- Target: `Days for shipping (real)`.
- Holdout: latest 20% of rows in date order (36,104 rows; 2017-04-22 to 2018-01-31).

## Holdout metrics
| Model                    |   MAE (days) |   RMSE (days) |   R-squared |
|:-------------------------|-------------:|--------------:|------------:|
| Median baseline          |        1.393 |         1.690 |      -0.094 |
| Ridge regression         |        0.985 |         1.265 |       0.387 |
| Decision tree (depth 10) |        0.990 |         1.272 |       0.380 |

## Notes
The model is an educational prototype, not a production delivery guarantee. The late-rate metric is explicitly defined as actual shipping days greater than scheduled shipping days and must be validated against the official SLA. Customer identifiers and post-outcome fields are excluded from model features.

## Run
Install dependencies:
```bash
pip install pandas numpy scikit-learn matplotlib
```
Place `DataCoSupplyChainDataset.csv` beside the script and run:
```bash
python Week_4_Logistics_Modeling.py
```
