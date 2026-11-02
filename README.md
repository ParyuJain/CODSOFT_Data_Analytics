# CODSOFT Data Analytics Internship

**Repository for CodSoft Data Analytics Internship Tasks**

This repository contains solutions for **at least 3 tasks** as required for successful completion of the internship.

---

## Tasks Completed

| Task | Title | Status |
|------|-------|--------|
| **Task 1** | Data Cleaning & Preprocessing | ✅ Completed |
| **Task 2** | Exploratory Data Analysis (EDA) | 🔄 In Progress |
| **Task 3** | Data Visualization Dashboard | ⏳ Pending |

---

## Task 1: Data Cleaning & Preprocessing

**Folder:** [`Task1/`](./Task1/)

### What was done
- Used the classic **Titanic** dataset (891 passengers)
- Inspected structure, data types, and summary statistics
- Identified missing values (`age` ~20%, `deck` ~77%, `embarked` 2)
- Identified and removed duplicate records
- Handled missing values:
  - Age → median by passenger class + sex
  - Embarked / Embark town → mode
  - Deck → dropped (too many missing)
- Corrected data types (categorical columns)
- Saved cleaned dataset as `titanic_cleaned.csv`

### How to run
```bash
cd Task1
pip install pandas seaborn numpy
python task1_data_cleaning.py
```

The script will print a full report and generate `titanic_cleaned.csv`.

---

## Dataset
**Titanic** – survival prediction dataset commonly used in data science.

---

## Author
**Paryu Jain**  
CodSoft Data Analytics Intern

---

## Instructions Followed
- Separate GitHub repository for all tasks
- Clear code with comments
- Cleaned dataset saved (Bonus completed)
