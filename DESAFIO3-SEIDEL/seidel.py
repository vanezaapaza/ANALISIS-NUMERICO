import numpy as np

# Matriz de coeficientes C
C = np.array([
    [52, 20, 25],
    [30, 50, 20],
    [18, 30, 55]
])

# Vector de resultados D
D = np.array([4800, 5210, 5690])

# Número de incógnitas
m = len(D)

# Valores iniciales
y = np.zeros(m)

# Umbral de tolerancia
tol = 1e-5

# Número máximo de iteraciones
max_iters = 1000

def gauss_seidel(C, D, y, tol, max_iters):
    m = len(D)
    for it in range(max_iters):
        y_old = np.copy(y)
        for j in range(m):
            sum1 = np.dot(C[j, :j], y[:j])
            sum2 = np.dot(C[j, j+1:], y_old[j+1:])
            y[j] = (D[j] - sum1 - sum2) / C[j, j]
        # Verificar la convergencia
        norm = np.linalg.norm(y - y_old, ord=np.inf)
        if norm < tol:
            return y, it + 1
    return y, max_iters

# Ejecutar el método de Gauss-Seidel
sol, iters = gauss_seidel(C, D, y, tol, max_iters)

print(f"Solución encontrada después de {iters} iteraciones:")
print(f"y1 = {sol[0]:.5f}")
print(f"y2 = {sol[1]:.5f}")
print(f"y3 = {sol[2]:.5f}")
