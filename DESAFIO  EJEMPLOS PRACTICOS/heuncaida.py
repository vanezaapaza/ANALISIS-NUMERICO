import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros
m = 5  # masa (kg)
g = 9.81  # gravedad (m/s^2)
k = 0.05  # constante (kg/m)
v0 = 0  # velocidad inicial (m/s)
t0, t_final = 0, 15  # intervalo de tiempo (s)
h = 0.1  # tamaño de paso

# Ecuación diferencial
def velocity_derivative(t, v):
    return -g + (k / m) * v**2

# Método de Heun
t_values = np.arange(t0, t_final + h, h)
v_values = np.zeros_like(t_values)
v_values[0] = v0  # Condición inicial

for i in range(len(t_values) - 1):
    t_n = t_values[i]
    v_n = v_values[i]
    
    # Calcular pendientes
    k1 = velocity_derivative(t_n, v_n)
    v_predict = v_n + h * k1
    k2 = velocity_derivative(t_n + h, v_predict)
    
    # Actualizar velocidad
    v_values[i + 1] = v_n + (h / 2) * (k1 + k2)

# Guardar los resultados en un archivo Excel
data = {"Tiempo (s)": t_values, "Velocidad (m/s)": v_values}
df = pd.DataFrame(data)
df.to_excel("velocidad_caida_libre.xlsx", index=False)

# Mostrar los resultados en la consola
print("Resultados de la velocidad en caída libre (Método de Heun):")
print(df)

# Graficar resultados
plt.plot(t_values, v_values, label='Método de Heun', color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad del objeto en caída libre')
plt.legend()
plt.grid()
plt.show()
