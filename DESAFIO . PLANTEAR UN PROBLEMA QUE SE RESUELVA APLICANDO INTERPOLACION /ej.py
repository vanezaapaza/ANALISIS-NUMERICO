import numpy as np
import matplotlib.pyplot as plt

# Datos de los días y alturas
dias = np.array([0, 1, 3, 4, 6])
alturas = np.array([3, 5, 10, 12, 18])

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term = term * (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Predicción de la altura en el día 2
dia_prediccion = 2
altura_predicha = lagrange_interpolation(dia_prediccion, dias, alturas)

# Imprimir resultado
print(f'La altura predicha para el día {dia_prediccion} es {altura_predicha:.2f} cm.')

# Visualización de los datos y la interpolación
x_vals = np.linspace(min(dias), max(dias), 100)
y_vals = [lagrange_interpolation(x, dias, alturas) for x in x_vals]

plt.scatter(dias, alturas, color='red', label='Datos originales')
plt.plot(x_vals, y_vals, label='Interpolación')
plt.scatter(dia_prediccion, altura_predicha, color='green', label=f'Predicción día {dia_prediccion}')
plt.xlabel('Días')
plt.ylabel('Altura (cm)')
plt.title('Interpolación de Lagrange para predicción de crecimiento de la planta')
plt.legend()
plt.grid(True)
plt.show()