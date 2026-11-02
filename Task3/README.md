# Task 3: Data Visualization Dashboard

## CodSoft Data Analytics Internship

### Objective
- Create meaningful visualizations using **Matplotlib**, **Seaborn**, and **Plotly**
- Design bar charts, line charts, pie charts, histograms, and scatter plots
- Customize charts with titles, labels, legends, and color schemes
- Present insights through clear visualizations
- **Bonus:** Interactive Plotly charts

### Dataset
Cleaned **Titanic** dataset (from Task 1) – 773 passengers

### Charts Created

| # | Chart | Type | File |
|---|-------|------|------|
| 1 | Survival Rate by Passenger Class | Bar | `01_survival_by_class.png` |
| 2 | Survival Rate by Sex | Bar | `02_survival_by_sex.png` |
| 3 | Passenger Count by Class & Sex | Grouped Bar | `03_count_by_class_sex.png` |
| 4 | Overall Survival Distribution | Pie | `04_overall_survival_pie.png` |
| 5 | Passengers by Embarkation Port | Pie | `05_embarkation_pie.png` |
| 6 | Age Distribution | Histogram + KDE | `06_age_histogram.png` |
| 7 | Fare Distribution | Histogram | `07_fare_histogram.png` |
| 8 | Age vs Fare (colored by Survival) | Scatter | `08_age_vs_fare_scatter.png` |
| 9 | Survival Rate by Age Group | Line | `09_survival_by_age_line.png` |
| 10 | Correlation Heatmap | Heatmap | `10_correlation_heatmap.png` |
| 11 | Fare by Class | Boxplot | `11_fare_boxplot_by_class.png` |
| 12 | Survival Rate by Class & Sex | Grouped Bar | `12_survival_class_sex.png` |

### Bonus – Interactive Charts (Plotly)
Running the script also generates interactive HTML files:
- `interactive_age_fare.html`
- `interactive_survival_class_sex.html`
- `interactive_survival_pie.html`

Open them in any browser for zoom, hover, and filter capabilities.

### Key Visual Insights
1. **Class matters** – Clear survival gradient: 1st > 2nd > 3rd class
2. **Gender gap** – Female survival ~3× higher than male
3. **Age pattern** – Children had relatively better survival odds
4. **Fare skew** – Most tickets were cheap; luxury fares are outliers
5. **Correlation** – Fare and Class show the strongest link to survival

### How to Run
```bash
pip install pandas seaborn matplotlib plotly numpy
python task3_visualization.py
```

All charts will be saved inside the `charts/` folder.

### Files
| File | Description |
|------|-------------|
| `task3_visualization.py` | Complete visualization script |
| `charts/` | All generated PNG + interactive HTML charts |
| `README.md` | This documentation |
