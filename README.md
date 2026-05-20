# Titanic Dataset Exploratory Data Analysis (EDA) using Seaborn & Matplotlib

## Overview
This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset using **Pandas, Seaborn, and Matplotlib**.  
The objective is to understand passenger demographics, survival patterns, fare distribution, age distribution, and relationships between different features.

The dataset is loaded directly from Seaborn:

```python
df = sns.load_dataset("titanic")
```

---

## Libraries Used

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

Required packages:

```bash
pip install pandas matplotlib seaborn
```

---

## Dataset Cleaning

### Missing Value Handling
- Removed `deck` column due to excessive missing values.
- Filled missing values in `age` with median age.

```python
df.drop(columns="deck", inplace=True)
df["age"] = df["age"].fillna(df["age"].median())
```

---

# Visualizations Included

## 1. Survival Count Plot
Displays total survivors and non-survivors.

**Plot Type:** Countplot

---

## 2. Gender Distribution
Shows number of male and female passengers.

**Plot Type:** Countplot

---

## 3. Survival Based on Gender
Compares survival rates between males and females.

**Plot Type:** Countplot with Hue

---

## 4. Passenger Count by Class
Displays number of passengers in:

- First Class
- Second Class
- Third Class

**Plot Type:** Countplot

---

## 5. Survival Based on Passenger Class
Analyzes effect of ticket class on survival.

**Plot Type:** Countplot + Hue

---

## 6. Age Distribution
Shows overall passenger age distribution.

**Plot Type:** Histogram

---

## 7. Survival vs Age
Checks whether age influenced survival.

**Plot Type:** Boxplot

---

## 8. Fare Distribution
Displays distribution of ticket fares.

**Plot Type:** Histogram

---

## 9. Fare Outlier Detection
Identifies extreme fare values.

**Plot Type:** Boxplot

---

## 10. Survival vs Fare
Compares fare paid with survival probability.

**Plot Type:** Boxplot

---

## 11. Correlation Heatmap
Shows correlations among numerical variables.

Features analyzed:

- Age
- Fare
- SibSp
- Parch
- Pclass
- Survived

**Plot Type:** Heatmap

---

## 12. Pairplot
Visualizes pairwise relationships among:

- Survived
- Age
- Fare
- Passenger Class

**Plot Type:** Pairplot

---

## 13. Violin Plot (Age vs Survival)
Displays age distribution with density estimation.

**Plot Type:** Violin Plot

---

## 14. FacetGrid — Age Distribution by Gender
Separate histograms for male and female passengers.

**Plot Type:** FacetGrid + Histogram

---

## 15. FacetGrid — Gender + Survival + Age
Age distributions split by:

- Gender
- Survival Status

**Plot Type:** FacetGrid + Hue

---

## 16. Scatter Plot (Age vs Fare)
Examines relationship between:

- Passenger Age
- Ticket Fare
- Survival

**Plot Type:** Scatterplot

---

## 17. Regression Plot (Age vs Fare)
Adds regression trend line.

**Plot Type:** Regplot

---

## 18. Swarm Plot (Class vs Age)
Displays passenger ages across classes.

**Plot Type:** Swarmplot

---

## 19. Catplot (Class vs Survival)
Survival comparison among ticket classes.

**Plot Type:** Catplot

---

## 20. Dashboard Visualization (Subplots)
Combines multiple plots:

- Survival Count
- Gender vs Survival
- Age Histogram
- Fare vs Class Boxplot

**Plot Type:** Subplots (2×2)

---

## 21. Plot Styling
Applied global styling:

```python
sns.set_style('whitegrid')
sns.set_context('talk')
sns.set_palette('pastel')
```

Improves readability and appearance.

---

# Key Insights Possible from Analysis

Examples of observations:

- Females had higher survival rates.
- First-class passengers survived more frequently.
- Most passengers were aged between 20–40.
- Fare distribution contains significant outliers.
- Higher ticket fares often correlate with better survival probability.

---

# Project Structure

```bash
Titanic-EDA/
│
├── titanic_analysis.py      # Main Python script
├── README.md                # Project documentation
└── visualizations/          # Saved plots (optional)
```

---

# Run Project

Execute:

```bash
python main.py
```

Uncomment:

```python
plt.show()
```

to display visualizations.

---

# Learning Outcomes

This project helps practice:

✔ Data Cleaning  
✔ Missing Value Handling  
✔ Exploratory Data Analysis  
✔ Seaborn Visualizations  
✔ Matplotlib Styling  
✔ Correlation Analysis  
✔ Statistical Visualization  
✔ Multi-plot Dashboards  

---

# Author

Created as a practice project for learning **Python Data Analysis and Visualization**.
