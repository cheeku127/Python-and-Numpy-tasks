import pandas as pd

# Provided dictionary and DataFrame
data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Department": ["CS", "CS", "IT", "IT", "CS", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 70000, 75000, 40000, 45000],
    "Experience": [2, 4, 3, 5, 6, 7, 1, 2]
}

df = pd.DataFrame(data)

# 1. Calculate the average salary for each department
avg_salary = df.groupby("Department")["Salary"].mean()
print("1. Average Salary per Department:")
print(avg_salary)

# 2. Calculate the maximum salary for each department
max_salary = df.groupby("Department")["Salary"].max()
print("\n2. Maximum Salary per Department:")
print(max_salary)

# 3. Calculate the minimum salary for each department
min_salary = df.groupby("Department")["Salary"].min()
print("\n3. Minimum Salary per Department:")
print(min_salary)

# 4. Calculate the average experience for each department
avg_exp = df.groupby("Department")["Experience"].mean()
print("\n4. Average Experience per Department:")
print(avg_exp)

# 5. Find the department with the highest average salary
highest_avg_dept = avg_salary.idxmax()
print(f"\n5. Department with the highest average salary: {highest_avg_dept} ({avg_salary[highest_avg_dept]:.2f})")

# 6. Count employees in each department
emp_count = df.groupby("Department")["Employee"].count()
print("\n6. Employee count per Department:")
print(emp_count)

# 7. Sort departments by average salary (descending)
sorted_dept_salary = avg_salary.sort_values(ascending=False)
print("\n7. Departments sorted by Average Salary:")
print(sorted_dept_salary)