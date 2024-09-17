import numpy as np

# Definimos los coeficientes del sistema de ecuaciones
A = np.array([[3, -0.1, -0.2], 
              [0.1, 7, -0.3], 
              [0.3, -0.2, 10]])

b = np.array([7.85, -19.3, 71.4])

# Valores iniciales de las incógnitas
x = np.array([0.0, 0.0, 0.0])

# Número máximo de iteraciones y tolerancia
max_iter = 100
tolerance = 1e-6

# Método de Gauss-Seidel
def gauss_seidel(A, b, x, max_iter, tolerance):
    n = len(b)
    for k in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            sum_Ax = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_Ax) / A[i][i]
        
        # Verificamos la tolerancia
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            print(f"Convergencia alcanzada en {k+1} iteraciones.")
            return x_new
        
        x = x_new
    print("El método no convergió después del número máximo de iteraciones.")
    return x

# Ejecutamos el método
solucion = gauss_seidel(A, b, x, max_iter, tolerance)

# Mostramos la solución
print("Solución aproximada:", solucion)
