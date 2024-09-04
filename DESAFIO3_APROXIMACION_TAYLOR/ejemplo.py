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
    for n in range(N + 1):
        term = (f.diff(x, n).subs(x, a) / sp.factorial(n)) * (x - a)**n
        taylor_approx += term

    return taylor_approx

# Definición de los datos (ejemplo)
x = sp.symbols('x')
f = sp.sin(x)  # Ejemplo: función seno

a = 0  # Punto de expansión
N = 5  # Orden de la aproximación
x_value = sp.pi / 4  # Valor específico de x (por ejemplo, pi/4)

# Cálculo de la serie de Taylor
taylor_approx = taylor_series(f, x, a, N)
taylor_evaluated = taylor_approx.subs(x, x_value)  # Evaluar la serie en x_value

print(f"\nSerie de Taylor de {f} alrededor de {a} hasta el orden {N}:")
print(taylor_approx)
print(f"\nEvaluación de la serie de Taylor en x = {x_value}:")
print(taylor_evaluated)
