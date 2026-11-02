# CODSOFT Data Analytics Internship

**Repository for CodSoft Data Analytics Internship Tasks**

This repository contains solutions for **at least 3 tasks** as required for successful completion of the internship.

---

## Tasks Completed

| Task | Title | Status |
|------|-------|--------|
| **Task 1** | Data Cleaning & Preprocessing | ✅ Completed |
| **Task 2** | Exploratory Data Analysis (EDA) | ✅ Completed |
| **Task 3** | Data Visualization Dashboard | ⏳ Pending |

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

### What was done
- Descriptive statistics for all features
- Distributions of Age and Fare
- Correlation analysis and crosstabs
- Outlier detection using IQR method
- Answered 5 key business questions
- **Bonus:** Written EDA report (`EDA_Report.txt`)

```bash
cd Task2
python task2_eda.py
```

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
└── README.md
```
