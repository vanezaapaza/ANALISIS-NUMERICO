# Definir la función para calcular el caudal usando la fórmula de Manning
def caudal_manning(n, A, Rh, S):
    return (1/n) * A * (Rh**(2/3)) * (S**0.5)


# Asignar valores a las variables - estos son valores de ejemplo
n = 0.03  # Coeficiente de rugosidad de Manning
A = 10    # Área de la sección transversal (m^2)
Rh = 5    # Radio hidráulico (m)
S = 0.01  # Pendiente

# Calcular el caudal usando la fórmula de Manning
Q = caudal_manning(n, A, Rh, S)
print(f"El caudal Q es: {Q} m^3/s")
