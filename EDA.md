# Code for EDA

```
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned Titanic dataset
df = pd.read_csv("titanic_cleaned.csv")

# Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())

# Step 1: Dataset Overview
# General info about the dataset
print("\nDataset Info:")
print(df.info())

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Step 2: Univariate Analysis
# Visualize the distribution of numerical features
numerical_cols = ['Age', 'Fare', 'Family_Size']

for col in numerical_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# Count plot for categorical variables
categorical_cols = ['Sex', 'Passenger_Class', 'Is_Alone', 'Survived']

for col in categorical_cols:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=col, palette='viridis')
    plt.title(f'Count Plot for {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()

# Step 3: Multivariate Analysis
# Correlation heatmap for numerical columns
plt.figure(figsize=(8, 6))
correlation_matrix = df[['Age', 'Fare', 'Family_Size', 'Survived']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title('Correlation Heatmap')
plt.show()

# Box plot to study relationship between 'Passenger_Class' and 'Fare'
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='Passenger_Class', y='Fare', palette='coolwarm')
plt.title('Passenger Class vs Fare')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

# Violin plot for 'Age' distribution by 'Survived'
plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x='Survived', y='Age', palette='muted', split=True)
plt.title('Age Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.show()

# Step 4: Survival Analysis
# Survival rates based on 'Sex'
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Sex', y='Survived', palette='rocket')
plt.title('Survival Rates by Sex')
plt.xlabel('Sex')
plt.ylabel('Survival Rate')
plt.show()

# Survival rates based on 'Passenger_Class'
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Passenger_Class', y='Survived', palette='Blues')
plt.title('Survival Rates by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# Step 5: Advanced Analysis
# Pairplot for selected features
selected_features = ['Age', 'Fare', 'Survived', 'Passenger_Class', 'Family_Size']
sns.pairplot(df[selected_features], hue='Survived', palette='husl', diag_kind='kde')
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()

# Survival rates based on 'Family_Size'
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Family_Size', y='Survived', palette='viridis')
plt.title('Survival Rate by Family Size')
plt.xlabel('Family Size')
plt.ylabel('Survival Rate')
plt.show()

# Step 6: Missing Values Visualization (if any)
# Uncomment this section if there are missing values
# import missingno as msno
# plt.figure(figsize=(8, 6))
# msno.matrix(df)
# plt.title('Missing Values Heatmap')
# plt.show()

# Step 7: Insights
# Calculate survival rates based on various groups
survival_by_sex = df.groupby('Sex')['Survived'].mean()
survival_by_class = df.groupby('Passenger_Class')['Survived'].mean()
survival_by_family = df.groupby('Family_Size')['Survived'].mean()

print("\nSurvival Rates by Sex:")
print(survival_by_sex)

print("\nSurvival Rates by Passenger Class:")
print(survival_by_class)

print("\nSurvival Rates by Family Size:")
print(survival_by_family)
```

Detailed Steps and Outputs
### Dataset Overview:

Get the basic structure of the dataset with info() and describe().
Check the distribution and ranges of numerical features.
### Univariate Analysis:

Visualize individual feature distributions using histograms and count plots.
Understand how numerical features like Age, Fare, etc., are spread.
For categorical features like Sex, Passenger_Class, visualize their counts.
### Multivariate Analysis:

Use correlation heatmaps to identify relationships between numerical variables.
Study relationships between categorical and numerical variables using box plots and violin plots.
### Survival Analysis:

Explore how survival rates differ across groups like Sex, Passenger_Class, and Family_Size.
Use bar plots to visualize survival trends.
### Advanced Analysis:

Create a pairplot to identify clusters and relationships between selected features.
Explore how survival is affected by combinations of variables.
### Missing Values Visualization:

Use libraries like missingno to visualize missing values, if any.
### Insights:

Compute group-level survival rates to draw actionable insights.
