"""
CodSoft Data Analytics Internship
Task 2: Exploratory Data Analysis (EDA)

Dataset: Cleaned Titanic dataset (from Task 1)
Objectives:
- Load a dataset and examine its features using descriptive statistics
- Identify trends, distributions, and relationships between variables
- Detect outliers and unusual patterns within the data
- Use summary statistics to answer key business questions
- Bonus: Create a short report highlighting your findings
"""

import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# 1. LOAD DATASET
# ============================================================
print("=" * 70)
print("TASK 2: EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 70)

# Prefer cleaned dataset from Task 1; fall back to fresh load + quick clean
try:
    df = pd.read_csv('../Task1/titanic_cleaned.csv')
    print("\nLoaded cleaned dataset from Task 1")
except FileNotFoundError:
    print("\nTask 1 cleaned file not found – loading & applying quick clean")
    df = sns.load_dataset('titanic')
    # Quick clean (same logic as Task 1)
    df['age'] = df.groupby(['pclass', 'sex'])['age'].transform(lambda x: x.fillna(x.median()))
    df['age'] = df['age'].fillna(df['age'].median())
    df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
    df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
    df = df.drop(columns=['deck'], errors='ignore')
    df = df.drop_duplicates()

print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# ============================================================
# 2. DESCRIPTIVE STATISTICS
# ============================================================
print("\n\n" + "=" * 70)
print("2. DESCRIPTIVE STATISTICS")
print("=" * 70)

print("\n--- Numerical Features ---")
print(df.describe().round(2))

print("\n--- Categorical Features ---")
cat_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns
print(df[cat_cols].describe())

print("\n--- Value Counts for Key Categorical Variables ---")
for col in ['survived', 'pclass', 'sex', 'embarked', 'who', 'alone']:
    if col in df.columns:
        print(f"\n{col.upper()}:")
        print(df[col].value_counts())
        print(f"  (Normalized %)\n{df[col].value_counts(normalize=True).mul(100).round(1)}")

# ============================================================
# 3. DISTRIBUTIONS & TRENDS
# ============================================================
print("\n\n" + "=" * 70)
print("3. DISTRIBUTIONS & TRENDS")
print("=" * 70)

print("\n--- Age Distribution ---")
print(f"Mean age   : {df['age'].mean():.1f}")
print(f"Median age : {df['age'].median():.1f}")
print(f"Std Dev    : {df['age'].std():.1f}")
print(f"Min / Max  : {df['age'].min():.1f} / {df['age'].max():.1f}")
print(f"Skewness   : {df['age'].skew():.2f}")

print("\n--- Fare Distribution ---")
print(f"Mean fare  : {df['fare'].mean():.2f}")
print(f"Median fare: {df['fare'].median():.2f}")
print(f"Std Dev    : {df['fare'].std():.2f}")
print(f"Min / Max  : {df['fare'].min():.2f} / {df['fare'].max():.2f}")
print(f"Skewness   : {df['fare'].skew():.2f}  (highly right-skewed)")

print("\n--- Survival Rate Overall ---")
survival_rate = df['survived'].mean() * 100
print(f"Overall survival rate: {survival_rate:.1f}%")

print("\n--- Survival Rate by Passenger Class ---")
print(df.groupby('pclass')['survived'].agg(['count', 'sum', 'mean']).round(3))
print("  (mean = survival rate)")

print("\n--- Survival Rate by Sex ---")
print(df.groupby('sex')['survived'].agg(['count', 'sum', 'mean']).round(3))

print("\n--- Survival Rate by Embarkation Port ---")
print(df.groupby('embarked')['survived'].agg(['count', 'sum', 'mean']).round(3))

print("\n--- Survival Rate by Who (man/woman/child) ---")
print(df.groupby('who')['survived'].agg(['count', 'sum', 'mean']).round(3))

print("\n--- Survival Rate by Alone vs With Family ---")
print(df.groupby('alone')['survived'].agg(['count', 'sum', 'mean']).round(3))

# ============================================================
# 4. RELATIONSHIPS BETWEEN VARIABLES
# ============================================================
print("\n\n" + "=" * 70)
print("4. RELATIONSHIPS BETWEEN VARIABLES")
print("=" * 70)

print("\n--- Correlation Matrix (Numerical) ---")
num_cols = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
corr = df[num_cols].corr().round(3)
print(corr)

print("\nKey correlations with Survival:")
print(corr['survived'].sort_values(ascending=False))

print("\n--- Cross-tab: Sex vs Class vs Survival ---")
print(pd.crosstab(index=[df['sex'], df['pclass']], columns=df['survived'],
                  margins=True, normalize='index').round(3))

print("\n--- Average Age by Class and Sex ---")
print(df.groupby(['pclass', 'sex'])['age'].mean().round(1).unstack())

print("\n--- Average Fare by Class ---")
print(df.groupby('pclass')['fare'].agg(['mean', 'median', 'min', 'max']).round(2))

# ============================================================
# 5. OUTLIER DETECTION
# ============================================================
print("\n\n" + "=" * 70)
print("5. OUTLIER DETECTION")
print("=" * 70)

def detect_outliers_iqr(series, name):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = series[(series < lower) | (series > upper)]
    print(f"\n{name}:")
    print(f"  Q1={Q1:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f}")
    print(f"  Lower bound={lower:.2f}, Upper bound={upper:.2f}")
    print(f"  Number of outliers: {len(outliers)} ({len(outliers)/len(series)*100:.1f}%)")
    if len(outliers) > 0:
        print(f"  Outlier range: {outliers.min():.2f} → {outliers.max():.2f}")
    return outliers

age_outliers = detect_outliers_iqr(df['age'], "AGE")
fare_outliers = detect_outliers_iqr(df['fare'], "FARE")

print("\n--- Unusual Patterns ---")
print(f"• Passengers with fare = 0 : {(df['fare'] == 0).sum()} (staff / complimentary?)")
print(f"• Children (age < 1)      : {(df['age'] < 1).sum()}")
print(f"• Elderly (age > 65)      : {(df['age'] > 65).sum()}")
print(f"• Large families (sibsp+parch >= 5): {((df['sibsp'] + df['parch']) >= 5).sum()}")

# ============================================================
# 6. KEY BUSINESS QUESTIONS ANSWERED
# ============================================================
print("\n\n" + "=" * 70)
print("6. KEY BUSINESS / ANALYTICAL QUESTIONS")
print("=" * 70)

print("""
Q1: What was the overall survival rate?
A1: {:.1f}% of passengers survived.

Q2: Did passenger class affect survival?
A2: Yes – 1st class had the highest survival rate ({:.1f}%), 
    followed by 2nd ({:.1f}%), then 3rd ({:.1f}%).

Q3: Was there a gender difference in survival?
A3: Strong difference – Female survival rate {:.1f}% vs Male {:.1f}%.
    "Women and children first" policy is clearly visible.

Q4: Did traveling alone affect survival chances?
A4: Passengers traveling alone had a lower survival rate ({:.1f}%)
    compared to those with family ({:.1f}%).

Q5: Which group had the best survival chances?
A5: Women in 1st class had the highest survival rate.
""".format(
    survival_rate,
    df[df['pclass']==1]['survived'].mean()*100,
    df[df['pclass']==2]['survived'].mean()*100,
    df[df['pclass']==3]['survived'].mean()*100,
    df[df['sex']=='female']['survived'].mean()*100,
    df[df['sex']=='male']['survived'].mean()*100,
    df[df['alone']==True]['survived'].mean()*100,
    df[df['alone']==False]['survived'].mean()*100
))

# ============================================================
# 7. BONUS – SHORT REPORT
# ============================================================
print("\n\n" + "=" * 70)
print("7. BONUS: SHORT EDA REPORT")
print("=" * 70)

report = f"""
TITANIC DATASET – EXPLORATORY DATA ANALYSIS REPORT
==================================================

Dataset Overview
----------------
• Rows after cleaning : {df.shape[0]}
• Columns             : {df.shape[1]}
• Overall survival    : {survival_rate:.1f}%

Key Findings
------------
1. Survival was strongly influenced by socio-economic status (class)
   and gender. First-class passengers and females had much higher
   survival rates.

2. Age distribution is roughly normal with a slight right skew.
   Median age ≈ {df['age'].median():.0f} years. Children and the elderly
   show different survival patterns.

3. Fare is highly right-skewed (many cheap tickets, few very expensive
   ones). Extreme high fares are present but expected for luxury cabins.

4. Passengers traveling with family had better survival odds than those
   traveling alone – likely due to mutual assistance during evacuation.

5. Outliers exist mainly in the Fare column (luxury tickets) and a few
   extreme ages. These are genuine data points, not errors.

Business / Historical Insight
-----------------------------
The data confirms the historical "women and children first" protocol
and the advantage of higher social class during the disaster. These
patterns are useful for understanding survival bias and can be used
as features in predictive models.

Recommendations for further work (Task 3)
-----------------------------------------
• Visualize survival rates by class, sex, and age groups
• Create age distribution histograms and fare boxplots
• Scatter plots of age vs fare colored by survival
• Heatmap of the correlation matrix
"""

print(report)

# Save report to file
with open('EDA_Report.txt', 'w') as f:
    f.write(report)
print("\n✅ Short report saved as: EDA_Report.txt")

print("\n" + "=" * 70)
print("TASK 2 COMPLETED SUCCESSFULLY")
print("=" * 70)
