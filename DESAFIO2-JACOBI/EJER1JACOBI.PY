import numpy as np

# Definición de la matriz A y el vector B
A = np.array([[52, 20, 25],
              [30, 50, 20],
              [18, 30, 55]], dtype=float)

B = np.array([[4800],
              [5210],
              [5690]], dtype=float)

# Parámetros de tolerancia y límite de iteraciones
tolerancia = 1e-10
max_iteraciones = 1000

# Verificación de la diagonal dominante
diagonal = np.abs(np.diag(A))
suma_filas = np.sum(np.abs(A), axis=1) - diagonal
if np.all(diagonal > suma_filas):
    print("La matriz es diagonal dominante. El método de Jacobi debería converger.")
else:
    print("La matriz no es diagonal dominante. El método de Jacobi podría no converger.")

# Inicialización de la solución
x = np.zeros_like(B)

# Implementación del método de Jacobi
for iteracion in range(max_iteraciones):
    x_nuevo = np.copy(x)  # Copia de la solución actual
    
    # Actualización de cada variable de la solución
    for i in range(A.shape[0]):
        suma = np.dot(A[i, :], x) - A[i, i] * x[i]
        x_nuevo[i] = (B[i] - suma) / A[i, i]
    
    # Verificación de la convergencia utilizando la norma infinita
    if np.linalg.norm(x_nuevo - x, ord=np.inf) < tolerancia:
        print(f"Convergencia alcanzada en {iteracion + 1} iteraciones.")
        x = x_nuevo  # Actualiza la solución final
        break
    
    x = x_nuevo  # Actualización para la siguiente iteración

else:
    print("No se alcanzó la convergencia dentro del límite de iteraciones.")

# Resultado final
print("Solución aproximada:", x)
