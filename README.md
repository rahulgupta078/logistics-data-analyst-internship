# Logistics Data Analyst Internship

**Internship Project | YuvaIntern | Logistics Data Analytics**

This repository documents my four-week Logistics Data Analyst Internship, where I explored logistics data, performed data preprocessing and analysis, created visualizations, and developed predictive models to support data-driven logistics decisions.

The project uses the **DataCo Smart Supply Chain dataset** to investigate shipping performance, delivery delays, operational patterns, and opportunities for logistics optimization.

## Internship Tasks

### Week 1 — Strategic Planning and Data Exploration

**Objective:** Understand the logistics business problem and establish an analytical plan.

**Work completed:**
- Identified key logistics challenges, including inventory management, route optimization, and supply chain coordination.
- Defined project objectives and relevant Key Performance Indicators (KPIs).
- Developed a roadmap for analyzing logistics operations.
- Outlined how data analysis can support better operational decisions.

**Deliverable:** Project planning and data exploration report.

[View Week 1](./Week-1/)

### Week 2 — Data Collection, Cleaning, and Preprocessing

**Objective:** Prepare logistics data for reliable analysis.

**Work completed:**
- Explored the DataCo Smart Supply Chain dataset.
- Reviewed data quality issues, missing values, and potential outliers.
- Described data cleaning, transformation, and normalization approaches.
- Prepared Python code examples and preprocessing steps for logistics analysis.

**Deliverable:** Data collection, cleaning, and preprocessing report.

[View Week 2](./Week-2/)

### Week 3 — Advanced Data Analysis and Visualization

**Objective:** Explore logistics data, identify patterns, and communicate findings through visualizations.

**Work completed:**
- Performed exploratory data analysis (EDA).
- Examined logistics performance indicators and relationships between relevant variables.
- Used statistical analysis and visualizations to investigate trends and potential operational bottlenecks.
- Documented findings and their implications for logistics decision-making.

**Deliverable:** Advanced data analysis and visualization report, with supporting charts and code where included.

[View Week 3](./Week-3/)

### Week 4 — Predictive Modeling and Optimization in Logistics Systems

**Objective:** Apply predictive modeling techniques to estimate shipping duration and recommend operational improvements.

**Work completed:**
- Analyzed 180,519 order-item records from the DataCo dataset.
- Selected relevant operational features while excluding customer-identifying information and post-outcome variables.
- Built and compared a median baseline, Ridge regression, and a constrained decision tree.
- Evaluated the models using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared on a chronological test set.
- Analyzed shipping performance by shipping mode and proposed logistics optimization strategies.

**Best tested model: Ridge Regression**

| Evaluation metric | Test result |
|---|---:|
| MAE | 0.985 days |
| RMSE | 1.265 days |
| R-squared | 0.387 |

The Ridge regression model achieved a lower prediction error than the median baseline. The results also highlight the need for additional operational data and further validation before real-world deployment.

**Deliverables:** Detailed report, Python implementation, evaluation charts, and optimization recommendations.

[View Week 4](./Week-4/)

## Technologies and Tools

- **Programming:** Python
- **Data analysis:** Pandas, NumPy
- **Visualization:** Matplotlib and Seaborn, where used in the project
- **Machine learning:** Scikit-learn
- **Documentation:** Microsoft Word, Markdown
- **Version control:** Git and GitHub

## Dataset

**Dataset:** DataCo Smart Supply Chain Dataset

The dataset contains order and shipping information used to study delivery duration, shipping modes, product categories, customer segments, and regional logistics performance.

The dataset is used for educational and analytical purposes. Refer to the dataset's original source and applicable usage terms when redistributing it.

## Repository Structure

```text
logistics-data-analyst-internship/
│
├── README.md
├── Week-1/
│   └── Planning and data exploration files
├── Week-2/
│   └── Data collection and preprocessing files
├── Week-3/
│   └── Analysis, visualizations, and report
└── Week-4/
    ├── README.md
    ├── Logistics_Data_Analyst_Week_4_Final_Report.docx
    ├── Week_4_Logistics_Modeling.py
    └── charts/
        ├── 01_late_rate_by_shipping_mode.png
        ├── 02_model_error_comparison.png
        └── 03_actual_vs_predicted.png
```

*Note: The folder contents shown above are representative. Keep the structure aligned with the files actually uploaded to the repository.*

## Key Learning Outcomes

- Understanding business problems in logistics and supply chain management.
- Preparing and exploring real-world datasets.
- Applying exploratory data analysis and data visualization.
- Building and evaluating regression models.
- Interpreting model results and identifying analytical limitations.
- Translating data-driven findings into practical operational recommendations.
- Organizing project deliverables and maintaining them using GitHub.

## Conclusion

This four-week internship provided practical experience across the data analytics workflow, from defining a business problem and preparing data to visualizing findings and evaluating predictive models. The project demonstrates how logistics data can help identify operational patterns, estimate shipping duration, and inform future optimization efforts.

**Disclaimer:** This repository is an educational internship project. Model results and recommendations should be validated with additional data before being used for operational decisions.

---

**Author:** Rahul Gupta  
**Field:** Data Analytics | Logistics Analytics | Machine Learning  
**Repository:** [Logistics Data Analyst Internship](https://github.com/rahulgupta078/logistics-data-analyst-internship)
