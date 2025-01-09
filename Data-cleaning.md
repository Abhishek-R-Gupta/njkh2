Here's a complete data cleaning workflow with detailed steps for the Titanic dataset. Each step addresses a key aspect of cleaning and preparing the data for analysis or model building.

## Code for Data Cleaning

```
# Import required libraries
import pandas as pd
import numpy as np

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# Display the first few rows
print("Initial Dataset:")
print(df.head())

# Step 1: Check for Missing Values
print("\nMissing Values (Before Cleaning):")
print(df.isnull().sum())

# Step 2: Handle Missing Values
# - Fill missing 'Age' values with the median
df['Age'] = df['Age'].fillna(df['Age'].median())

# - Fill missing 'Embarked' values with the mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# - Drop 'Cabin' column due to a large number of missing values
df = df.drop(columns=['Cabin'])

# Step 3: Check for Duplicates
print("\nDuplicate Rows (Before Cleaning):", df.duplicated().sum())
df = df.drop_duplicates()

# Step 4: Handle Outliers
# Use the Interquartile Range (IQR) method to detect and remove outliers in 'Fare'
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove rows where 'Fare' is an outlier
df = df[(df['Fare'] >= lower_bound) & (df['Fare'] <= upper_bound)]

# Step 5: Encode Categorical Variables
# Encode 'Sex' column (male=0, female=1)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Encode 'Embarked' column using one-hot encoding
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Step 6: Rename Columns for Clarity (optional)
df.rename(columns={'Pclass': 'Passenger_Class', 'SibSp': 'Siblings_Spouses', 'Parch': 'Parents_Children'}, inplace=True)

# Step 7: Feature Scaling
# Standardize 'Age' and 'Fare' to bring them to a similar scale
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Step 8: Check for Zero Variance Columns
zero_variance = df.loc[:, df.std() == 0]
print("\nZero Variance Columns (if any):")
print(zero_variance)

# Step 9: Create New Features (Feature Engineering)
# Create a 'Family_Size' feature
df['Family_Size'] = df['Siblings_Spouses'] + df['Parents_Children'] + 1

# Create a 'Is_Alone' feature (1 if alone, 0 otherwise)
df['Is_Alone'] = (df['Family_Size'] == 1).astype(int)

# Step 10: Remove Unnecessary Columns
# Drop columns that are irrelevant or redundant
df = df.drop(columns=['Name', 'Ticket'])

# Final Dataset Summary
print("\nCleaned Dataset Summary:")
print(df.info())
print(df.head())
```

Explanation of Steps
## Missing Values:

Replace missing values in numeric columns (e.g., Age) with the median.
Replace missing values in categorical columns (e.g., Embarked) with the mode.
Drop columns with excessive missing values (e.g., Cabin).
Duplicates:

## Remove duplicate rows to avoid redundancy in data.
Outliers:

Detect outliers using the IQR method and remove rows with outliers in Fare.
Encoding Categorical Variables:

Convert Sex into binary values (0/1).
Use one-hot encoding for the Embarked column.
## Feature Scaling:

Standardize Age and Fare for consistency in feature magnitudes.
## Feature Engineering:

Create new features (Family_Size and Is_Alone) for better model performance.
Column Renaming:

Rename columns for improved readability and understanding.
Removing Irrelevant Columns:

Drop columns like Name and Ticket that don’t add value to the analysis.
Additional Notes
This workflow covers all essential data cleaning steps.
You can further extend feature engineering based on domain knowledge, such as creating features like Title from the Name column.
Let me know if you need help extending or deploying this dataset!
