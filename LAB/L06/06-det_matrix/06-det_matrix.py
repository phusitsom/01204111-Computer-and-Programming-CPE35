from numpy import array, linalg
print(int(linalg.det(array([list(map(int, input(f"Row {i+1} : ").split()))for i in range(3)]))))
