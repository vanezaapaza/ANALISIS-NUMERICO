import numpy as np

# Definir la matriz de coeficientes A y el vector de términos independientes B
A = np.array([[1.5, 2, 1], [4, 3.5, 2], [2, 5, 10]])  # Cambios en la matriz A
B = np.array([15, 30, 50])  # Cambios en el vector B

# Resolver el sistema de ecuaciones (X = A^-1 * B)
X = np.linalg.solve(A, B)

# Calcular el determinante de A
determinante = np.linalg.det(A)

# Calcular la matriz condicional
condicional = np.linalg.cond(A)

# Imprimir resultados
print("Solución del sistema de ecuaciones: x =", X[0], ", y =", X[1], ", z =", X[2])
print("Determinante de la matriz A:", determinante)
print("Número condicional de la matriz A:", condicional)
