import pandas as pd

# Provided dictionary and DataFrame
data = {
    "Age": [20, 21, None, 24, None, 30],
    "Salary": [30000, None, 40000, 50000, None, 60000],
    "Experience": [1, 2, 3, None, 5, 6],
    "Department": ["CS", "IT", "CS", None, "IT", "CS"]
}

df = pd.DataFrame(data)

# 1. Display the DataFrame
print("1. Initial DataFrame:")
print(df)

# 2. Count missing values in every column
print("\n2. Missing values per column:")
print(df.isnull().sum())

# 3. Fill missing Age using the median
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# 4. Fill missing Salary using the median
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)

# 5. Fill missing Experience using the median
median_exp = df["Experience"].median()
df["Experience"] = df["Experience"].fillna(median_exp)

# 6. Fill missing Department using the mode
mode_dept = df["Department"].mode()[0]
df["Department"] = df["Department"].fillna(mode_dept)

# 7. Verify that there are no missing values
print("\n7. Missing values count after imputation (should all be 0):")
print(df.isnull().sum())

# 8. Print the cleaned DataFrame
print("\n8. Cleaned DataFrame:")
print(df)