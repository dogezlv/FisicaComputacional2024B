import numpy as np
import matplotlib.pyplot as plt

h_inicial = float(input("Ingrese la altura inicial (m): "))
v_inicial = float(input("Ingrese la velocidad inicial (m/s): "))
m = float(input("Ingrese la masa del objeto (kg): "))

g = 9.81

def energia_cinetica(m, v):
    return 0.5 * m * v**2

def energia_potencial(m, g, h):
    return m * g * h

alturas = np.linspace(h_inicial, 0, 100)
velocidades = np.sqrt(v_inicial**2 + 2 * g * (h_inicial - alturas))

energias_cineticas = energia_cinetica(m, velocidades)
energias_potenciales = energia_potencial(m, g, alturas)
energias_mecanicas = energias_cineticas + energias_potenciales

plt.plot(alturas, energias_cineticas, label="Energía Cinética ($E_K$)", color="blue")
plt.plot(alturas, energias_potenciales, label="Energía Potencial ($E_P$)", color="green")
plt.plot(alturas, energias_mecanicas, label="Energía Mecánica ($E_m$)", color="red", linestyle="--")

plt.xlabel("Altura (m)")
plt.ylabel("Energía (J)")
plt.title("Conservación de la Energía Mecánica")
plt.legend()
plt.grid(True)
plt.show()
