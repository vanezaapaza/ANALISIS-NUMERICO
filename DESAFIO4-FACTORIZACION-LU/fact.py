import numpy as np
from scipy.linalg import lu

# Definimos la matriz M y el vector N
M = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]])

N = np.array([27, -61.5, -21.5])

# Realizamos la descomposición LU
P, L, U = lu(M)

# Mostrar las matrices L y U
print("Matriz L:")
print(L)

print("\nMatriz U:")
print(U)

# Resolver el sistema L * z = N
z = np.linalg.solve(L, N)

# Resolver el sistema U * w = z
w = np.linalg.solve(U, z)

print("\nSolución del sistema:")
print(w)
