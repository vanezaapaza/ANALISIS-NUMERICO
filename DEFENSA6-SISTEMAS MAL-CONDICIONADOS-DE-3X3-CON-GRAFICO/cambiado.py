import numpy as np

# Nueva matriz de coeficientes A con cambios significativos
A_modificada = np.array([[2.5, 1.5, 1], [3.5, 2, 3.5], [1.5, 4.5, 9]])  # cambios en algunos elementos
B = np.array([10, 25, 30])

# Resolver el sistema de ecuaciones modificado
X_modificada = np.linalg.solve(A_modificada, B)

# Calcular el determinante de la nueva matriz
determinante_modificado = np.linalg.det(A_modificada)

# Calcular el número condicional de la nueva matriz
condicional_modificado = np.linalg.cond(A_modificada)

# Imprimir resultados
print("Solución del sistema de ecuaciones (modificada): x =", X_modificada[0], ", y =", X_modificada[1], ", z =", X_modificada[2])
print("Determinante de la matriz modificada A:", determinante_modificado)
print("Número condicional de la matriz modificada A:", condicional_modificado)
