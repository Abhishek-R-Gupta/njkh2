# NumPy
**Creating an array**

```
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
```
Creates a NumPy array from a list for efficient numerical operations.

**Generating random numbers**
```
random_numbers = np.random.rand(5)
```
Generates an array of 5 random numbers between 0 and 1.

**Reshaping an array**

```
reshaped_array = arr.reshape(1, 5)
```
Reshapes a 1D array into a 2D array (1 row, 5 columns).

**Matrix multiplication**
```
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
result = np.dot(mat1, mat2)
```
Performs matrix multiplication.

**Finding unique elements**

```
unique_elements = np.unique([1, 2, 2, 3])
```
Finds unique elements in an array.

**Finding mean, median, and standard deviation**
```
arr = np.array([1, 2, 3, 4])
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
```
Calculates the mean, median, and standard deviation of an array.

**Boolean indexing**

```
arr = np.array([1, 2, 3, 4])
filtered = arr[arr > 2]
```
Filters elements greater than 2 using a condition.

# Pandas
**Creating a DataFrame**

```
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
```
Creates a DataFrame to store structured data.

**Reading a CSV file**

```
df = pd.read_csv('data.csv')
```
Reads a CSV file into a DataFrame for analysis.

**Filtering rows**

```
filtered_df = df[df['Age'] > 25]
```
Filters rows where the 'Age' column value is greater than 25.

**Descriptive statistics**

```
stats = df.describe()
```
Provides summary statistics for numerical columns.

**Adding a new column**

```
df['Salary'] = [50000, 60000]
```
Adds a new column to the DataFrame.

**Dropping a column**

```
df = df.drop('Salary', axis=1)
```
Drops the 'Salary' column from the DataFrame.

**Handling missing values**

```
df = df.fillna(0)
```
Fills missing values with 0.

# Matplotlib
**Line Plot**

```
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
plt.title('Line Plot')
plt.show()
```
Creates a simple line plot to visualize data.

**Bar Plot**

```
plt.bar(['A', 'B', 'C'], [5, 7, 3])
plt.title('Bar Plot')
plt.show()
```
Creates a bar plot to compare categorical data.

**Histogram**

```
data = [1, 2, 2, 3, 3, 3, 4]
plt.hist(data, bins=4)
plt.title('Histogram')
plt.show()
```
Creates a histogram to show data distribution.

**Scatter Plot**

```
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()
```
Visualizes relationships between two variables with a scatter plot.

