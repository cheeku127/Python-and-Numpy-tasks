import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

#Print shape, dimensions, and data type

print("Shape:", X.shape)
print("Dimensions:", X.ndim)
print("Data type:", X.dtype)

#Extract the second column

print(X[:,1])

#Extract the first two rows

print(X[0:2])

#Extract the last two columns

print(X[:,-2:])

#Replace all values greater than 80 with 0

X[X > 80] = 0
print(X)

#Calculate each column's minimum, maximum, mean, and standard deviation

print("Column minimum:", np.min(X, axis=0))
print("Column maximum:", np.max(X, axis=0))
print("Column mean:", np.mean(X, axis=0))
print("Column standard deviation:", np.std(X, axis=0))