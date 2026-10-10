# Week 3 – Advanced Data Analysis and Visualization

## Objective
Explore the DataCo supply-chain dataset and analyze delivery time, late-delivery rates, shipping mode, monthly volume, and available commercial indicators.

## Dataset
- Source file: `DataCoSupplyChainDataset.csv` (public DataCo Smart Supply Chain dataset)
- 180,519 order-item records and 53 columns in the original table
- Note: records are order items, not guaranteed unique shipments. A direct transportation-cost column was not identified, so sales values are not treated as freight costs.

## Work performed
- Calculated descriptive statistics and delay days (actual minus scheduled shipping days)
- Compared delivery performance by shipping mode
- Reviewed monthly order-item volume and regional late rates
- Calculated Pearson correlations for selected numeric fields
- Created six charts and documented interpretations, limitations, and recommendations

## Files
- `Logistics_Data_Analyst_Week_3_Final_Report.docx` – final report
- `Week_3_Logistics_Analysis.py` – Python analysis script
- `Week_3_Analysis_Assets/` – generated chart images

## Tools
Python, pandas, NumPy, Matplotlib

