"""
CodSoft Data Analytics Internship
Task 1: Data Cleaning & Preprocessing

Dataset: Titanic (from seaborn)
Objective:
- Import a dataset using Python and inspect its structure
- Identify missing values, duplicate records, and inconsistent data entries
- Clean the dataset by handling null values, removing duplicates, and correcting data types
- Prepare the data for further analysis using Pandas
- Bonus: Save the cleaned dataset as a new CSV file
"""

import pandas as pd
import numpy as np
import seaborn as sns

# ============================================================
# 1. IMPORT DATASET AND INSPECT STRUCTURE
# ============================================================
print("=" * 60)
print("TASK 1: DATA CLEANING & PREPROCESSING")
print("=" * 60)

# Load the Titanic dataset
df = sns.load_dataset('titanic')

print("\n1. DATASET IMPORT & INITIAL INSPECTION")
print("-" * 40)
print(f"Shape of dataset: {df.shape[0]} rows × {df.shape[1]} columns")
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nData types:")
print(df.dtypes)

print("\nBasic info:")
df.info()

print("\nDescriptive statistics (numerical columns):")
print(df.describe())

print("\nDescriptive statistics (categorical columns):")
print(df.describe(include=['object', 'category', 'bool']))

# ============================================================
# 2. IDENTIFY MISSING VALUES, DUPLICATES, AND INCONSISTENCIES
# ============================================================
print("\n\n2. IDENTIFYING DATA QUALITY ISSUES")
print("-" * 40)

# Missing values
print("\nMissing values per column:")
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
missing_df = pd.DataFrame({
    'Missing Count': missing,
    'Missing %': missing_pct
})
print(missing_df[missing_df['Missing Count'] > 0])

# Duplicate records
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")
print(f"Percentage of duplicates: {(df.duplicated().sum() / len(df) * 100):.2f}%")

# Inconsistencies / observations
print("\nPotential inconsistencies / notes:")
print("- 'alive' column is redundant with 'survived' (yes/no vs 0/1)")
print("- 'class' is the categorical version of 'pclass'")
print("- 'embark_town' is the full name version of 'embarked'")
print("- 'deck' has >77% missing values → candidate for dropping")
print("- 'age' has ~20% missing values → needs imputation")

# Unique values check for key categorical columns
print("\nUnique values in key columns:")
for col in ['sex', 'embarked', 'class', 'who', 'alive', 'embark_town']:
    print(f"  {col}: {df[col].unique().tolist()}")

# ============================================================
# 3. CLEAN THE DATASET
# ============================================================
print("\n\n3. DATA CLEANING STEPS")
print("-" * 40)

df_clean = df.copy()

# --- 3.1 Handle Missing Values ---
print("\n3.1 Handling Missing Values...")

# Age: Impute with median age grouped by passenger class and sex
# (more realistic than overall median)
print("  - Imputing 'age' with median by pclass + sex")
df_clean['age'] = df_clean.groupby(['pclass', 'sex'])['age'].transform(
    lambda x: x.fillna(x.median())
)
# Fallback for any remaining NaNs
df_clean['age'] = df_clean['age'].fillna(df_clean['age'].median())

# Embarked & embark_town: fill with mode (most frequent)
print("  - Filling 'embarked' and 'embark_town' with mode")
mode_embarked = df_clean['embarked'].mode()[0]
df_clean['embarked'] = df_clean['embarked'].fillna(mode_embarked)

mode_town = df_clean['embark_town'].mode()[0]
df_clean['embark_town'] = df_clean['embark_town'].fillna(mode_town)

# Deck: >70% missing → drop the column
print("  - Dropping 'deck' column (>77% missing)")
df_clean = df_clean.drop(columns=['deck'])

print("  Missing values after imputation:")
print(df_clean.isnull().sum())

# --- 3.2 Remove Duplicates ---
print("\n3.2 Removing Duplicate Records...")
duplicates_before = df_clean.duplicated().sum()
print(f"  Duplicates before: {duplicates_before}")
df_clean = df_clean.drop_duplicates()
print(f"  Duplicates after:  {df_clean.duplicated().sum()}")
print(f"  Rows removed:      {duplicates_before}")

# --- 3.3 Correct Data Types ---
print("\n3.3 Correcting Data Types...")
df_clean['sex'] = df_clean['sex'].astype('category')
df_clean['embarked'] = df_clean['embarked'].astype('category')
df_clean['class'] = df_clean['class'].astype('category')
df_clean['who'] = df_clean['who'].astype('category')
df_clean['embark_town'] = df_clean['embark_town'].astype('category')
df_clean['alive'] = df_clean['alive'].astype('category')

# Ensure numerical columns are correct
df_clean['age'] = df_clean['age'].astype(float)
df_clean['fare'] = df_clean['fare'].astype(float)
df_clean['survived'] = df_clean['survived'].astype(int)
df_clean['pclass'] = df_clean['pclass'].astype(int)

print("  Updated data types:")
print(df_clean.dtypes)

# ============================================================
# 4. PREPARE DATA FOR FURTHER ANALYSIS
# ============================================================
print("\n\n4. FINAL CLEANED DATASET READY FOR ANALYSIS")
print("-" * 40)
print(f"Final shape: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")
print("\nMissing values check (should all be 0):")
print(df_clean.isnull().sum())
print("\nSample of cleaned data:")
print(df_clean.head(10))

# ============================================================
# 5. BONUS: SAVE CLEANED DATASET
# ============================================================
print("\n\n5. SAVING CLEANED DATASET")
print("-" * 40)

output_path = 'titanic_cleaned.csv'
df_clean.to_csv(output_path, index=False)
print(f"✅ Cleaned dataset saved as: {output_path}")

# Also save a summary
summary = {
    'original_rows': df.shape[0],
    'original_columns': df.shape[1],
    'cleaned_rows': df_clean.shape[0],
    'cleaned_columns': df_clean.shape[1],
    'rows_removed_duplicates': duplicates_before,
    'columns_dropped': ['deck'],
    'missing_age_imputed': 177,
    'missing_embarked_imputed': 2
}
print("\nCleaning Summary:")
for k, v in summary.items():
    print(f"  {k}: {v}")

print("\n" + "=" * 60)
print("TASK 1 COMPLETED SUCCESSFULLY")
print("=" * 60)
