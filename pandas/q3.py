import pandas as pd

# Provided dictionary and DataFrame
data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Math": [80, 60, 90, 70, 85, 55],
    "Science": [75, 65, 95, 72, 80, 60],
    "English": [85, 70, 88, 75, 90, 50]
}

df = pd.DataFrame(data)

# 1. Create an Average column
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 2. Create a Total column
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# 3. Create a Passed column (Average >= 60 -> True, Average < 60 -> False)
df["Passed"] = df["Average"] >= 60

print("Updated DataFrame with Average, Total, and Passed columns:")
print(df)
print("-" * 50)

# 4. Find the student with the highest average
best_student = df.loc[df["Average"].idxmax()]
print(f"4. Student with highest average: {best_student['Name']} ({best_student['Average']:.2f})")

# 5. Find students whose average is >= 80
high_scorers = df[df["Average"] >= 80]
print("\n5. Students with Average >= 80:")
print(high_scorers)

# 6. Sort by average in descending order
df_sorted = df.sort_values(by="Average", ascending=False)
print("\n6. Sorted by Average (Descending):")
print(df_sorted)

# 7. Calculate the overall average
overall_avg = df["Average"].mean()
print(f"\n7. Overall Average across all students: {overall_avg:.2f}")

# 8. Display only Name, Average, and Passed
print("\n8. Selected Columns (Name, Average, Passed):")
print(df[["Name", "Average", "Passed"]])