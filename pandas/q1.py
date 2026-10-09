import pandas as pd

# Provided dictionary and DataFrame
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 22, 30, 28],
    "Marks": [85, 72, 90, 65, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

# 1. Print the first 3 rows
print("1. First 3 rows:")
print(df.head(3))

# 2. Print the last 2 rows
print("\n2. Last 2 rows:")
print(df.tail(2))

# 3. Print the shape
print("\n3. Shape:")
print(df.shape)

# 4. Print the column names
print("\n4. Column names:")
print(df.columns.tolist())

# 5. Print the data types
print("\n5. Data types:")
print(df.dtypes)

# 6. Select only Name and Marks
print("\n6. Name and Marks:")
print(df[["Name", "Marks"]])

# 7. Select students whose marks are > 80
print("\n7. Students with marks > 80:")
print(df[df["Marks"] > 80])

# 8. Sort students by marks from highest to lowest
print("\n8. Sorted by marks (descending):")
print(df.sort_values(by="Marks", ascending=False))