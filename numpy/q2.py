import numpy as np

# Create the given 2D NumPy array (5 rows, 3 columns / features)
X = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000],
    [40, 400, 4000],
    [50, 500, 5000]
])

# Compute the mean of each feature/column

mean = np.mean(X, axis=0)
print("Column means:", mean)

# Compute the standard deviation of each feature/column
std = np.std(X, axis=0)
print("Column standard deviations:", std)

# Standardize each feature using NumPy broadcasting: (X - mean) / std
X_scaled = (X - mean) / std

#  Displaying the resulting standardized feature matrix
print("Standardized matrix:\n", X_scaled)

#  Verifying the standardization

print("Scaled means:", np.mean(X_scaled, axis=0))

# The standard deviation of each scaled column should be 1.0
print("Scaled standard deviations:", np.std(X_scaled, axis=0))