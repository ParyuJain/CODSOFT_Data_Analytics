"""
CodSoft Data Analytics Internship
Task 3: Data Visualization Dashboard

Dataset: Cleaned Titanic dataset (from Task 1 / Task 2)
Objectives:
- Create meaningful visualizations using Matplotlib, Seaborn (and Plotly)
- Design bar charts, line charts, pie charts, histograms, and scatter plots
- Customize charts with titles, labels, legends, and color schemes
- Present insights through clear and easy-to-understand visualizations
- Bonus: Interactive visualizations with Plotly
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Try to import plotly for interactive charts (bonus)
try:
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    print("Plotly not installed – static charts only. (pip install plotly for interactive bonus)")

# Style settings
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# ============================================================
# 1. LOAD DATA
# ============================================================
print("=" * 70)
print("TASK 3: DATA VISUALIZATION DASHBOARD")
print("=" * 70)

try:
    df = pd.read_csv('../Task1/titanic_cleaned.csv')
    print("Loaded cleaned dataset from Task 1")
except FileNotFoundError:
    print("Loading & applying quick clean...")
    df = sns.load_dataset('titanic')
    df['age'] = df.groupby(['pclass', 'sex'])['age'].transform(lambda x: x.fillna(x.median()))
    df['age'] = df['age'].fillna(df['age'].median())
    df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
    df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
    df = df.drop(columns=['deck'], errors='ignore')
    df = df.drop_duplicates()

print(f"Shape: {df.shape}")

# Create output folder for charts
import os
os.makedirs('charts', exist_ok=True)

# ============================================================
# 2. BAR CHARTS
# ============================================================
print("\nCreating Bar Charts...")

# 2.1 Survival rate by Passenger Class
fig, ax = plt.subplots(figsize=(8, 5))
survival_by_class = df.groupby('pclass')['survived'].mean() * 100
colors = ['#2ecc71', '#f39c12', '#e74c3c']
bars = ax.bar(survival_by_class.index.astype(str), survival_by_class.values, color=colors, edgecolor='black')
ax.set_title('Survival Rate by Passenger Class', fontweight='bold', pad=15)
ax.set_xlabel('Passenger Class')
ax.set_ylabel('Survival Rate (%)')
ax.set_ylim(0, 80)
for bar, val in zip(bars, survival_by_class.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5, f'{val:.1f}%',
            ha='center', va='bottom', fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/01_survival_by_class.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 01_survival_by_class.png")

# 2.2 Survival rate by Sex
fig, ax = plt.subplots(figsize=(7, 5))
survival_by_sex = df.groupby('sex')['survived'].mean() * 100
colors_sex = ['#e74c3c', '#3498db']
bars = ax.bar(survival_by_sex.index.str.title(), survival_by_sex.values, color=colors_sex, edgecolor='black', width=0.6)
ax.set_title('Survival Rate by Sex', fontweight='bold', pad=15)
ax.set_xlabel('Sex')
ax.set_ylabel('Survival Rate (%)')
ax.set_ylim(0, 90)
for bar, val in zip(bars, survival_by_sex.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f'{val:.1f}%',
            ha='center', va='bottom', fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/02_survival_by_sex.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 02_survival_by_sex.png")

# 2.3 Count of passengers by Class and Sex (grouped bar)
fig, ax = plt.subplots(figsize=(9, 5))
ct = pd.crosstab(df['pclass'], df['sex'])
ct.plot(kind='bar', ax=ax, color=['#e74c3c', '#3498db'], edgecolor='black')
ax.set_title('Passenger Count by Class and Sex', fontweight='bold', pad=15)
ax.set_xlabel('Passenger Class')
ax.set_ylabel('Count')
ax.legend(title='Sex', labels=['Female', 'Male'])
ax.set_xticklabels(['1st', '2nd', '3rd'], rotation=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/03_count_by_class_sex.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 03_count_by_class_sex.png")

# ============================================================
# 3. PIE CHARTS
# ============================================================
print("\nCreating Pie Charts...")

# 3.1 Overall Survival
fig, ax = plt.subplots(figsize=(7, 7))
surv_counts = df['survived'].value_counts()
ax.pie(surv_counts, labels=['Did Not Survive', 'Survived'], autopct='%1.1f%%',
       colors=['#e74c3c', '#2ecc71'], startangle=90, explode=(0.03, 0.03),
       shadow=True, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax.set_title('Overall Survival Distribution', fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/04_overall_survival_pie.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 04_overall_survival_pie.png")

# 3.2 Embarkation Port distribution
fig, ax = plt.subplots(figsize=(7, 7))
embark_counts = df['embarked'].value_counts()
ax.pie(embark_counts, labels=['Southampton (S)', 'Cherbourg (C)', 'Queenstown (Q)'],
       autopct='%1.1f%%', colors=['#3498db', '#9b59b6', '#1abc9c'],
       startangle=90, explode=(0.02, 0.02, 0.02), shadow=True,
       textprops={'fontsize': 11})
ax.set_title('Passengers by Embarkation Port', fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/05_embarkation_pie.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 05_embarkation_pie.png")

# ============================================================
# 4. HISTOGRAMS
# ============================================================
print("\nCreating Histograms...")

# 4.1 Age distribution
fig, ax = plt.subplots(figsize=(9, 5))
sns.histplot(df['age'], bins=30, kde=True, color='#3498db', edgecolor='black', ax=ax)
ax.axvline(df['age'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["age"].mean():.1f}')
ax.axvline(df['age'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["age"].median():.1f}')
ax.set_title('Age Distribution of Passengers', fontweight='bold', pad=15)
ax.set_xlabel('Age (years)')
ax.set_ylabel('Frequency')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/06_age_histogram.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 06_age_histogram.png")

# 4.2 Fare distribution
fig, ax = plt.subplots(figsize=(9, 5))
sns.histplot(df['fare'], bins=40, kde=True, color='#e67e22', edgecolor='black', ax=ax)
ax.set_title('Fare Distribution (Highly Right-Skewed)', fontweight='bold', pad=15)
ax.set_xlabel('Fare')
ax.set_ylabel('Frequency')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/07_fare_histogram.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 07_fare_histogram.png")

# ============================================================
# 5. SCATTER PLOTS
# ============================================================
print("\nCreating Scatter Plots...")

# 5.1 Age vs Fare colored by Survival
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(df['age'], df['fare'], c=df['survived'], cmap='RdYlGn',
                     alpha=0.6, edgecolors='black', linewidth=0.3, s=40)
ax.set_title('Age vs Fare (colored by Survival)', fontweight='bold', pad=15)
ax.set_xlabel('Age')
ax.set_ylabel('Fare')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Survived (0 = No, 1 = Yes)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/08_age_vs_fare_scatter.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 08_age_vs_fare_scatter.png")

# 5.2 Age vs Survival probability (line chart)
fig, ax = plt.subplots(figsize=(9, 5))
df['age_bin'] = pd.cut(df['age'], bins=[0, 12, 18, 30, 50, 80], labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
survival_by_age = df.groupby('age_bin', observed=True)['survived'].mean() * 100
ax.plot(survival_by_age.index.astype(str), survival_by_age.values, marker='o', linewidth=2.5,
        markersize=10, color='#8e44ad')
ax.set_title('Survival Rate by Age Group (Line Chart)', fontweight='bold', pad=15)
ax.set_xlabel('Age Group')
ax.set_ylabel('Survival Rate (%)')
ax.set_ylim(0, 70)
for i, v in enumerate(survival_by_age.values):
    ax.text(i, v + 2, f'{v:.1f}%', ha='center', fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/09_survival_by_age_line.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 09_survival_by_age_line.png")

# ============================================================
# 6. ADDITIONAL INSIGHTFUL CHARTS
# ============================================================
print("\nCreating Additional Insight Charts...")

# 6.1 Heatmap of correlations
fig, ax = plt.subplots(figsize=(8, 6))
num_cols = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f',
            square=True, linewidths=0.5, ax=ax, cbar_kws={'shrink': 0.8})
ax.set_title('Correlation Heatmap', fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('charts/10_correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 10_correlation_heatmap.png")

# 6.2 Boxplot – Fare by Class
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='pclass', y='fare', palette=['#2ecc71', '#f39c12', '#e74c3c'], ax=ax)
ax.set_title('Fare Distribution by Passenger Class', fontweight='bold', pad=15)
ax.set_xlabel('Passenger Class')
ax.set_ylabel('Fare')
ax.set_xticklabels(['1st', '2nd', '3rd'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/11_fare_boxplot_by_class.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 11_fare_boxplot_by_class.png")

# 6.3 Survival by Class and Sex
fig, ax = plt.subplots(figsize=(9, 5))
survival_class_sex = df.groupby(['pclass', 'sex'])['survived'].mean().unstack() * 100
survival_class_sex.plot(kind='bar', ax=ax, color=['#e74c3c', '#3498db'], edgecolor='black')
ax.set_title('Survival Rate by Class and Sex', fontweight='bold', pad=15)
ax.set_xlabel('Passenger Class')
ax.set_ylabel('Survival Rate (%)')
ax.legend(title='Sex', labels=['Female', 'Male'])
ax.set_xticklabels(['1st', '2nd', '3rd'], rotation=0)
ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/12_survival_class_sex.png', dpi=150, bbox_inches='tight')
plt.close()
print("  \u2713 12_survival_class_sex.png")

# ============================================================
# 7. BONUS – INTERACTIVE PLOTLY CHARTS (if available)
# ============================================================
if PLOTLY_AVAILABLE:
    print("\nCreating Interactive Plotly charts (Bonus)...")

    # Interactive scatter
    fig = px.scatter(df, x='age', y='fare', color='survived',
                     color_continuous_scale='RdYlGn',
                     title='Interactive: Age vs Fare by Survival',
                     labels={'survived': 'Survived', 'age': 'Age', 'fare': 'Fare'},
                     hover_data=['pclass', 'sex'])
    fig.write_html('charts/interactive_age_fare.html')
    print("  \u2713 interactive_age_fare.html")

    # Interactive bar – survival by class & sex
    surv = df.groupby(['pclass', 'sex'])['survived'].mean().reset_index()
    surv['survived'] = surv['survived'] * 100
    fig = px.bar(surv, x='pclass', y='survived', color='sex', barmode='group',
                 title='Interactive: Survival Rate by Class and Sex',
                 labels={'survived': 'Survival Rate (%)', 'pclass': 'Class', 'sex': 'Sex'},
                 color_discrete_map={'female': '#e74c3c', 'male': '#3498db'})
    fig.write_html('charts/interactive_survival_class_sex.html')
    print("  \u2713 interactive_survival_class_sex.html")

    # Interactive pie
    fig = px.pie(df, names='survived', title='Interactive: Overall Survival',
                 color='survived', color_discrete_map={0: '#e74c3c', 1: '#2ecc71'},
                 labels={'survived': 'Survived'})
    fig.write_html('charts/interactive_survival_pie.html')
    print("  \u2713 interactive_survival_pie.html")
else:
    print("\n(Plotly not available – skipping interactive charts)")

# ============================================================
# 8. SUMMARY OF INSIGHTS
# ============================================================
print("\n" + "=" * 70)
print("VISUALIZATION INSIGHTS SUMMARY")
print("=" * 70)
print("""
1. Survival by Class (Bar): Clear gradient – 1st class highest, 3rd lowest.
2. Survival by Sex (Bar): Females survived at ~3× the rate of males.
3. Overall Survival (Pie): Only ~41.5% of passengers survived.
4. Age Distribution (Histogram): Peak in 20–30s, few elderly.
5. Fare Distribution (Histogram): Strong right skew – most tickets cheap.
6. Age vs Fare (Scatter): Higher fares cluster with higher survival (green).
7. Survival by Age Group (Line): Children had relatively better odds.
8. Correlation Heatmap: Fare & Class show strongest link to survival.
9. Fare by Class (Boxplot): Large spread in 1st class; many outliers.
10. Class × Sex (Grouped Bar): 1st-class women had the best survival rate.
""")

print("\u2705 All charts saved in the 'charts/' folder")
print("=" * 70)
print("TASK 3 COMPLETED SUCCESSFULLY")
print("=" * 70)
