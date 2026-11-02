# CODSOFT Data Analytics Internship

**Repository for CodSoft Data Analytics Internship Tasks**

This repository contains solutions for **3 tasks** as required for successful completion of the internship.

---

## Tasks Completed

| Task | Title | Status |
|------|-------|--------|
| **Task 1** | Data Cleaning & Preprocessing | ✅ Completed |
| **Task 2** | Exploratory Data Analysis (EDA) | ✅ Completed |
| **Task 3** | Data Visualization Dashboard | ✅ Completed |

---

## Task 1: Data Cleaning & Preprocessing

**Folder:** [`Task1/`](./Task1/)

- Used the classic **Titanic** dataset
- Handled missing values, removed duplicates, corrected data types
- Cleaned dataset ready for analysis

```bash
cd Task1
python task1_data_cleaning.py
```

---

## Task 2: Exploratory Data Analysis (EDA)

**Folder:** [`Task2/`](./Task2/)

### Key Findings
| Metric | Value |
|--------|-------|
| Overall survival rate | **41.5%** |
| 1st Class survival | **64.1%** |
| Female survival | **73.9%** |
| Male survival | **22.0%** |
| Alone vs Family | 34.2% vs 51.0% |

- Descriptive statistics, distributions, correlations, outlier detection
- Answered key business questions
- **Bonus:** Written EDA report

```bash
cd Task2
python task2_eda.py
```

---

## Task 3: Data Visualization Dashboard

**Folder:** [`Task3/`](./Task3/)

### Charts Created (12 static + 3 interactive)
- **Bar charts**: Survival by Class, Survival by Sex, Count by Class & Sex
- **Pie charts**: Overall Survival, Embarkation Port
- **Histograms**: Age distribution, Fare distribution
- **Scatter plot**: Age vs Fare colored by Survival
- **Line chart**: Survival Rate by Age Group
- **Heatmap**: Correlation matrix
- **Boxplot**: Fare by Class
- **Bonus**: Interactive Plotly HTML charts (hover, zoom, filter)

```bash
cd Task3
pip install plotly   # for interactive bonus charts
python task3_visualization.py
```

All charts are saved in the `charts/` folder when you run the script.

---

## Dataset
**Titanic** – classic survival prediction dataset

---

## Author
**Paryu Jain**  
CodSoft Data Analytics Intern

---

## Repository Structure
```
CODSOFT_Data_Analytics/
├── Task1/
│   ├── task1_data_cleaning.py
│   └── README.md
├── Task2/
│   ├── task2_eda.py
│   ├── EDA_Report.txt
│   └── README.md
├── Task3/
│   ├── task3_visualization.py
│   └── README.md
└── README.md
```
