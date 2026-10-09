import numpy as np

# Initial array (Columns represent Age, Salary)
X = np.array([
    [25, 50000],
    [17, 30000],
    [35, 80000],
    [42, 90000],
    [19, 25000],
    [31, 70000]
])

print("Original Array:\n", X)
print("-" * 50)

# 1. Find people whose age is >= 25
age_mask = X[:, 0] >= 25
people_age_25 = X[age_mask]
print("1. People with Age >= 25:\n", people_age_25)

# 2. Find people whose salary is > 60000
salary_mask = X[:, 1] > 60000
people_salary_60k = X[salary_mask]
print("\n2. People with Salary > 60,000:\n", people_salary_60k)

# 3. Find people whose age is >= 25 AND salary is > 60000
combined_mask = (X[:, 0] >= 25) & (X[:, 1] > 60000)
people_combined = X[combined_mask]
print("\n3. People with Age >= 25 AND Salary > 60,000:\n", people_combined)

# 4. Replace salaries below 30000 with 30000
# (Operating on a copy or directly in-place)
X_modified = X.copy()
X_modified[X_modified[:, 1] < 30000, 1] = 30000
print("\n4. Array after replacing salaries < 30,000 with 30,000:\n", X_modified)

# 5. Calculate the average salary (using the modified array or original array)
avg_salary = np.mean(X[:, 1])
print(f"\n5. Average Salary (Original): {avg_salary:.2f}")

# 6. Calculate the average salary only for people aged >= 25
avg_salary_age_25 = np.mean(X[X[:, 0] >= 25, 1])
print(f"6. Average Salary for Age >= 25: {avg_salary_age_25:.2f}")