import numpy as np
import sympy as sp

def validar_funcion(expr):
    x, y = sp.symbols('x y')
    func_simb = sp.sympify(expr)
    if func_simb.is_constant():
        return False
    if func_simb == x or func_simb == y:
        return False
    return True

def obtener_funcion_personalizada():
    while True:
        expr = input("Introduce la función de la fuerza (en términos de x): ")
        if validar_funcion(expr):
            return expr
        else:
            print("Función inválida. No puede ser constante ni simplemente 'x' o 'y'. Inténtalo de nuevo.")

def calcular_trabajo_suma(f, a, b, n):
    x_vals = np.linspace(a, b, n+1)
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(x_vals[i]) * dx
    return suma

def calcular_trabajo_integral(f):
    x = sp.symbols('x')
    trabajo_exacto = sp.integrate(f(x), (x, 0, 1))
    return trabajo_exacto

def comparar_trabajos(exacto, aproximado):
    C = abs((exacto - aproximado) / exacto) * 100
    return C

def main():
    expr = obtener_funcion_personalizada()
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(expr), "numpy")
    a = 0
    b = 1
    n = 100
    trabajo_aproximado = calcular_trabajo_suma(f, a, b, n)
    trabajo_exacto = calcular_trabajo_integral(sp.sympify(expr))
    print(f"Trabajo (integral exacta): {trabajo_exacto}")
    print(f"Trabajo (sumatoria): {trabajo_aproximado}")
    C = comparar_trabajos(trabajo_exacto, trabajo_aproximado)
    print(f"Diferencia porcentual: {C}%")

if __name__ == "__main__":
    main()
