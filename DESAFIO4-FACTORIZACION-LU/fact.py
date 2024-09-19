import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la nueva matriz C y el vector D
C = np.array([[5, 1, -2],
              [3, -4, 1],
              [2, 2, 3]])

D = np.array([10, -15, 5])

# Crear la figura para el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear una cuadrícula de puntos en el espacio (x2, x3)
x2, x3 = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))

# Definir los tres planos usando las ecuaciones Cx = D
# Ecuaciones:  C[0,0]*x1 + C[0,1]*x2 + C[0,2]*x3 = D[0]
x1_1 = (D[0] - C[0,1]*x2 - C[0,2]*x3) / C[0,0]
x1_2 = (D[1] - C[1,1]*x2 - C[1,2]*x3) / C[1,0]
x1_3 = (D[2] - C[2,1]*x2 - C[2,2]*x3) / C[2,0]

# Graficar los tres planos
ax.plot_surface(x2, x3, x1_1, alpha=0.5, rstride=100, cstride=100, color='blue')
ax.plot_surface(x2, x3, x1_2, alpha=0.5, rstride=100, cstride=100, color='green')
ax.plot_surface(x2, x3, x1_3, alpha=0.5, rstride=100, cstride=100, color='red')

# Solución del sistema
x_sol = np.linalg.solve(C, D)

# Graficar la solución como un punto
ax.scatter(x_sol[1], x_sol[2], x_sol[0], color='black', s=100, label=f"Solución ({x_sol[1]:.2f}, {x_sol[2]:.2f}, {x_sol[0]:.2f})")

# Etiquetas y límites de los ejes
ax.set_xlabel('x2')
ax.set_ylabel('x3')
ax.set_zlabel('x1')

plt.title('Intersección de los tres planos (solución)')
plt.legend()
plt.show()
