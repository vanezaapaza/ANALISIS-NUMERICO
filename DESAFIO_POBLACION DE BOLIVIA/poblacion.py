# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Datos
años_historicos = np.array([1950, 1976, 1992, 2001, 2012, 2019])
poblacion_historica = np.array([2704165, 4613419, 6420792, 8274325, 10059856, 10694075])

def interpolacion_newton(datos_x, datos_y, valor_x):
    n = len(datos_x)
    coeficientes = np.zeros((n, n))
    coeficientes[:, 0] = datos_y

    for j in range(1, n):
        for i in range(n - j):
            coeficientes[i][j] = (coeficientes[i + 1][j - 1] - coeficientes[i][j - 1]) / (datos_x[i + j] - datos_x[i])

    resultado = coeficientes[0, 0]
    producto = 1

    for j in range(1, n):
        producto *= (valor_x - datos_x[j - 1])
        resultado += coeficientes[0, j] * producto

    return resultado

# Predecir la población para un año futuro
año_estimado = 2024
poblacion_estimada = interpolacion_newton(años_historicos, poblacion_historica, año_estimado)

print(f"La población estimada para el año {año_estimado} es: {poblacion_estimada:.0f}")

# Gráfica mejorada
plt.figure(figsize=(10, 6))

# Puntos de datos conocidos
plt.scatter(años_historicos, poblacion_historica, color='red', label='Datos conocidos', s=100, edgecolor='black')

# Línea que conecta los puntos históricos
plt.plot(años_historicos, poblacion_historica, color='red', linestyle='-', linewidth=2)

# Predicción para el año 2024
plt.scatter(año_estimado, poblacion_estimada, color='blue', label='Predicción para 2024', s=150, edgecolor='black', zorder=5)

# Líneas verticales y horizontales desde el punto de predicción
plt.axvline(x=año_estimado, color='blue', linestyle='--', linewidth=1)
plt.axhline(y=poblacion_estimada, color='blue', linestyle='--', linewidth=1)

# Etiquetas adicionales
for i in range(len(años_historicos)):
    plt.text(años_historicos[i], poblacion_historica[i], f'{poblacion_historica[i]:,}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

plt.text(año_estimado, poblacion_estimada, f'{int(poblacion_estimada):,}', fontsize=12, verticalalignment='bottom', horizontalalignment='left')

# Título y etiquetas
plt.title('Interpolación de Newton para la población de Bolivia', fontsize=16)
plt.xlabel('Años', fontsize=14)
plt.ylabel('Población', fontsize=14)

# Leyenda y cuadrícula
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
