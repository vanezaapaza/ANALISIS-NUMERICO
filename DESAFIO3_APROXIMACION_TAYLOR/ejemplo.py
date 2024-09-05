import sympy as sp

def taylor_series(f, x, a, N):
    """
    Calcula la aproximación de Taylor de la función f(x) alrededor del punto a hasta el orden N.

    :param f: Función a aproximar
    :param x: Variable independiente
    :param a: Punto de expansión
    :param N: Orden de la aproximación de Taylor
    :return: Expresión de la serie de Taylor
    """
    taylor_approx = 0
    terms = []
    for n in range(N + 1):
        term = (f.diff(x, n).subs(x, a) / sp.factorial(n)) * (x - a)**n
        taylor_approx += term
        terms.append(term)
    
    return taylor_approx, terms

# Definición de los datos
x = sp.symbols('x')
f = sp.sin(x)  # Ejemplo: función seno

a = 0.4  # Punto de expansión
N = 3  # Orden de la aproximación
x_value = 0.90  # Valor específico de x
tolerancia = 0.01  # Tolerancia aceptable del error

# Cálculo de la serie de Taylor y obtención de términos individuales
taylor_approx, terms = taylor_series(f, x, a, N)

# Mostrar el término x_0 (orden 0) y x_1 (orden 1)
x_0 = terms[0]  # Término constante
x_1 = terms[1]  # Término lineal

# Evaluación de la serie en x_value
taylor_evaluated = taylor_approx.subs(x, x_value)

# Valor exacto de la función
valor_exacto = f.subs(x, x_value)

# Cálculo del error absoluto
error = abs(valor_exacto - taylor_evaluated)

# Mostrar los resultados intermedios para depuración
print(f"Término x_0 (constante): {x_0}")
print(f"Término x_1 (lineal): {x_1}")

print(f"\nSerie de Taylor de {f} alrededor de {a} hasta el orden {N}:")
print(taylor_approx)

print(f"\nEvaluación de la serie de Taylor en x = {x_value}:")
print(taylor_evaluated)

print(f"\nValor exacto de la función en x = {x_value}:")
print(valor_exacto)

print(f"\nError: {error}")

# Comparación con la tolerancia
if error < tolerancia:
    mensaje = f"El error {error} está dentro de la tolerancia ({tolerancia})."
else:
    mensaje = f"El error {error} excede la tolerancia ({tolerancia})."

print(mensaje)
