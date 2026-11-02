# Task 1: Data Cleaning & Preprocessing

## CodSoft Data Analytics Internship

### Objective
Import a dataset, identify data quality issues (missing values, duplicates, inconsistencies), clean the data, and prepare it for further analysis using Pandas.

### Dataset
**Titanic Dataset** (from seaborn / classic Kaggle dataset)
- 891 passengers
- 15 original columns
- Contains realistic missing values and some duplicates

### Steps Performed

1. **Import & Inspect Structure**
   - Loaded dataset using `seaborn.load_dataset('titanic')`
   - Examined shape, dtypes, head/tail, and descriptive statistics

2. **Identify Issues**
   - Missing values:
     - `age`: 177 (~20%)
     - `deck`: 688 (~77%)
     - `embarked` / `embark_town`: 2 each
   - Duplicate rows: 107+
   - Redundant columns noted (`alive` ≈ `survived`, `class` ≈ `pclass`)

3. **Cleaning Actions**
   - **Age**: Imputed using median age grouped by `pclass` + `sex` (more accurate than overall median)
   - **Embarked / Embark_town**: Filled with mode
   - **Deck**: Dropped (too many missing values)
   - **Duplicates**: Removed
   - **Data types**: Converted categorical columns to `category` dtype for efficiency

4. **Bonus**
   - Running the script saves the cleaned dataset as `titanic_cleaned.csv`

### Files
| File | Description |
|------|-------------|
| `task1_data_cleaning.py` | Complete Python script with all steps and comments |

### How to Run
```bash
pip install pandas seaborn numpy
python task1_data_cleaning.py
```

The script will:
- Print a detailed cleaning report
- Generate `titanic_cleaned.csv` in the same folder

### Result
- Original: 891 rows × 15 columns
- Cleaned: 773 rows × 14 columns
- No missing values remaining
- Ready for Exploratory Data Analysis (Task 2)
