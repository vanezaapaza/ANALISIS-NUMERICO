import math

# Definir la serie de Taylor para ln(x) en x = 1
def taylor_ln(x, order):
    t = x - 1  # (x - 1) es un término común
    approximation = 0
    if order >= 1:
        approximation += t  # Primer orden
    if order >= 2:
        approximation -= (t**2) / 2  # Segundo orden
    if order >= 3:
        approximation += (t**3) / 3  # Tercer orden
    if order >= 4:
        approximation -= (t**4) / 4  # Cuarto orden
    return approximation

# Valor verdadero de ln(2.5)
true_value = math.log(2.5)

# Órdenes de aproximación
orders = [1, 2, 3, 4]
approximations = [taylor_ln(2.5, order) for order in orders]

# Calcular el error relativo porcentual verdadero para cada aproximación
errors = [abs((true_value - approx) / true_value) * 100 for approx in approximations]


# Mostrar los resultados
for i, order in enumerate(orders):
    print(f"Orden {order}:")
    print(f"Aproximación: {approximations[i]}")
    print(f"Error relativo porcentual verdadero: {errors[i]:.4f}%")
    print("-" * 30)

# Resultado del valor real de ln(2.5)
print(f"Valor verdadero de ln(2.5): {true_value}")
