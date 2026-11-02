# Task 2: Exploratory Data Analysis (EDA)

## CodSoft Data Analytics Internship

### Objective
- Load a dataset and examine its features using descriptive statistics
- Identify trends, distributions, and relationships between variables
- Detect outliers and unusual patterns
- Answer key business questions with summary statistics
- **Bonus:** Create a short report highlighting the findings

### Dataset
Cleaned **Titanic** dataset (from Task 1)  
773 passengers × 14 columns after cleaning

### Key Findings (Summary)

| Question | Insight |
|----------|--------|
| Overall survival rate | **41.5%** |
| Survival by Class | 1st: **64.1%** → 2nd: **50.6%** → 3rd: **26.0%** |
| Survival by Sex | Female: **73.9%** vs Male: **22.0%** |
| Alone vs Family | Alone: **34.2%** vs With family: **51.0%** |
| Strongest predictors | Passenger class & Gender |

### Analysis Performed

1. **Descriptive Statistics** – mean, median, std, min/max for numerical & categorical features
2. **Distributions** – Age (slightly right-skewed), Fare (highly right-skewed)
3. **Relationships** – Correlation matrix, crosstabs (Sex × Class × Survival)
4. **Outlier Detection** – IQR method on Age and Fare
5. **Business Questions** – 5 key questions answered with clear numbers
6. **Bonus Report** – `EDA_Report.txt` with structured findings

### Files
| File | Description |
|------|-------------|
| `task2_eda.py` | Complete EDA script with all steps and comments |
| `EDA_Report.txt` | Short written report of findings (Bonus) |
| `README.md` | This file |

### How to Run
```bash
pip install pandas seaborn numpy
python task2_eda.py
```

The script prints a full analysis to the console and saves `EDA_Report.txt`.

### Next Step
→ **Task 3: Data Visualization Dashboard** (charts based on these insights)
