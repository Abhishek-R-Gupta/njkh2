# Code for Feature Engineering

```
# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv("titanic_cleaned.csv")

# Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())

# Step 1: Creating New Features
# Feature: Family_Size (combining SibSp and Parch)
df['Family_Size'] = df['SibSp'] + df['Parch'] + 1

# Feature: Is_Alone (indicates if the passenger is traveling alone)
df['Is_Alone'] = (df['Family_Size'] == 1).astype(int)

# Feature: Fare_Per_Person (adjust fare based on family size)
df['Fare_Per_Person'] = df['Fare'] / df['Family_Size']

# Feature: Title (extract titles from names)
df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())

# Combine rare titles into 'Other'
rare_titles = ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
df['Title'] = df['Title'].replace(rare_titles, 'Other')
df['Title'] = df['Title'].replace({'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'})

# Step 2: Encoding Categorical Features
# Encoding 'Sex' using Label Encoding
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

# Encoding 'Embarked' using One-Hot Encoding
ohe = OneHotEncoder(drop='first', sparse=False)
embarked_encoded = pd.DataFrame(ohe.fit_transform(df[['Embarked']]), columns=ohe.get_feature_names_out(['Embarked']))
df = pd.concat([df, embarked_encoded], axis=1)
df.drop('Embarked', axis=1, inplace=True)

# Encoding 'Title' using One-Hot Encoding
title_encoded = pd.get_dummies(df['Title'], prefix='Title', drop_first=True)
df = pd.concat([df, title_encoded], axis=1)
df.drop('Title', axis=1, inplace=True)

# Step 3: Feature Transformation
# Log transformation of Fare to reduce skewness
df['Fare'] = df['Fare'].apply(lambda x: x if x == 0 else pd.np.log1p(x))

# Scaling numerical features
scaler = StandardScaler()
numerical_cols = ['Age', 'Fare', 'Family_Size', 'Fare_Per_Person']
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Step 4: Dropping Unnecessary Features
# Remove features that are unlikely to improve model performance
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Step 5: Final Dataset Preview
print("\nFinal Dataset Preview:")
print(df.head())

# Check the dataset info after feature engineering
print("\nDataset Info After Feature Engineering:")
print(df.info())

# Save the processed dataset to a new CSV file
df.to_csv("titanic_feature_engineered.csv", index=False)
```
Detailed Steps in Feature Engineering
### Creating New Features:

Family_Size: Total number of family members traveling together (SibSp + Parch + 1).
Is_Alone: Binary feature indicating if the passenger is traveling alone.
Fare_Per_Person: Adjusted fare based on the family size.
Title: Extracted from the Name field to capture honorifics like Mr., Mrs., etc., and grouped rare titles under "Other."
### Encoding Categorical Features:

Label Encoding: Converts binary categorical features (e.g., Sex) into 0s and 1s.
One-Hot Encoding: Expands multi-class categorical variables (e.g., Embarked, Title) into multiple binary columns.
### Feature Transformation:

Log Transformation: Applies logarithmic scaling to skewed numerical features (e.g., Fare) to normalize their distribution.
Standard Scaling: Standardizes numerical features (e.g., Age, Fare, etc.) to have a mean of 0 and a standard deviation of 1.
### Dropping Unnecessary Features:

Removed columns like PassengerId, Name, Ticket, and Cabin that are not directly useful for prediction.
### Final Dataset:

Ensures the dataset is clean, transformed, and ready for model training.
Notes:
Why create new features? To enhance the model's ability to capture hidden relationships in the data.

Why encode categorical features? Machine learning models cannot handle raw categorical data; encoding converts them into numerical formats.

Why log-transform features? It reduces the skewness of data, which is especially important for features like Fare.

Why scale numerical features? Features with different scales can negatively impact models like Logistic Regression or SVM.
