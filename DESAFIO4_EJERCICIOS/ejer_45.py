import sympy as sp

# Definir la variable y función
x = sp.symbols('x')
f = 25*x**3 - 6*x**2 + 7*x - 88

# Punto base y el punto a evaluar
a = 1  # punto base
x_eval = 3  # punto a predecir

# Calcular el valor exacto de f(3)
f_exact = f.subs(x, x_eval)

# Derivadas de f
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)
f_triple_prime = sp.diff(f_double_prime, x)

# Evaluar f y sus derivadas en x = 1
f_a = f.subs(x, a)
f_prime_a = f_prime.subs(x, a)
f_double_prime_a = f_double_prime.subs(x, a)
f_triple_prime_a = f_triple_prime.subs(x, a)

# Serie de Taylor hasta tercer orden
taylor_0 = f_a  # Aproximación de orden cero
taylor_1 = taylor_0 + f_prime_a * (x_eval - a)  # Primer orden
taylor_2 = taylor_1 + (f_double_prime_a / 2) * (x_eval - a)**2  # Segundo orden
taylor_3 = taylor_2 + (f_triple_prime_a / 6) * (x_eval - a)**3  # Tercer orden

# Evaluar las aproximaciones de Taylor
taylor_0_eval = taylor_0
taylor_1_eval = taylor_1
taylor_2_eval = taylor_2
taylor_3_eval = taylor_3

# Función para calcular el error relativo porcentual
def relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# Calcular los errores relativos
errors = {
    "0th order": relative_error(f_exact, taylor_0_eval),
    "1st order": relative_error(f_exact, taylor_1_eval),
    "2nd order": relative_error(f_exact, taylor_2_eval),
    "3rd order": relative_error(f_exact, taylor_3_eval),
}


# Mostrar resultados
print(f"Valor exacto de f(3): {f_exact}")
print(f"Aproximación de orden 0: {taylor_0_eval}")
print(f"Aproximación de orden 1: {taylor_1_eval}")
print(f"Aproximación de orden 2: {taylor_2_eval}")
print(f"Aproximación de orden 3: {taylor_3_eval}")
print("Errores relativos porcentuales:")
for order, error in errors.items():
    print(f"{order}: {error}%")
