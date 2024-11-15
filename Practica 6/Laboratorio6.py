import numpy as np
import matplotlib.pyplot as plt

L = float(input("Ingrese la longitud del dominio (L): "))
T = float(input("Ingrese el tiempo total de simulación (T): "))
dx = float(input("Ingrese el tamaño de paso en el espacio (dx): "))
dt = float(input("Ingrese el tamaño de paso en el tiempo (dt): "))

Nx = int(L / dx) + 1
Nt = int(T / dt) + 1
x = np.linspace(0, L, Nx)
r = dt / dx**2

def condicion_inicial(x):
    return np.sin(np.pi * x / L)

def condicion_contorno_izq(t):
    return 0

def condicion_contorno_der(t):
    return 0

def ecuacion_calor():
    u = np.zeros((Nx, Nt))
    u[:, 0] = condicion_inicial(x)
    
    for j in range(0, Nt - 1):
        u[0, j+1] = condicion_contorno_izq(j * dt)
        u[-1, j+1] = condicion_contorno_der(j * dt)
        for i in range(1, Nx - 1):
            u[i, j+1] = (1 - 2 * r) * u[i, j] + r * (u[i+1, j] + u[i-1, j])
    
    return u

def ecuacion_onda():
    u = np.zeros((Nx, Nt))
    u[:, 0] = condicion_inicial(x)
    u[:, 1] = u[:, 0]
    
    for j in range(1, Nt - 1):
        u[0, j+1] = condicion_contorno_izq(j * dt)
        u[-1, j+1] = condicion_contorno_der(j * dt)
        for i in range(1, Nx - 1):
            u[i, j+1] = (2 * (1 - r**2) * u[i, j] +
                         r**2 * (u[i+1, j] + u[i-1, j]) - u[i, j-1])
    
    return u

opcion = input("Seleccione la ecuación a resolver (calor/onda): ").strip().lower()
if opcion == "calor":
    u = ecuacion_calor()
elif opcion == "onda":
    u = ecuacion_onda()
else:
    print("Opción no válida. Seleccione 'calor' o 'onda'.")
    exit()

plt.plot(x, u[:, -1])
plt.xlabel("Posición x")
plt.ylabel("u(x, T)")
plt.title(f"Distribución final para la ecuación de {opcion}")
plt.show()
