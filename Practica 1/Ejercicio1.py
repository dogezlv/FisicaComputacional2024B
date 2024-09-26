def ecuacion_a(v, delta_t):
    delta_x = v * delta_t
    return delta_x

def ecuacion_b(vi, delta_t, alpha):
    delta_x = vi * delta_t + (alpha * delta_t**2) / 2
    return delta_x

def ecuacion_c(vi, alpha, delta_t):
    vf = vi + alpha * delta_t
    return vf

v = float(input("Ingrese la velocidad (v) para la ecuacion a): "))
vi = float(input("Ingrese la velocidad inicial (Vi) para las ecuaciones b) y c): "))
alpha = float(input("Ingrese la aceleración (α) para las ecuaciones b) y c): "))
delta_t = float(input("Ingrese el intervalo de tiempo (Δt) para las 3 ecuaciones: "))

delta_x_a = ecuacion_a(v, delta_t)
delta_x_b = ecuacion_b(vi, delta_t, alpha)
vf = ecuacion_c(vi, alpha, delta_t)

print(f"Resultado de la ecuación a) Δx = {delta_x_a}")
print(f"Resultado de la ecuación b) Δx = {delta_x_b}")
print(f"Resultado de la ecuación c) Vf = {vf}")
