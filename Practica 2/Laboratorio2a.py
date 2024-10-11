import numpy as np
import matplotlib.pyplot as plt

def orbita_planeta(masa_sol, distancia, periodo, nombre_planeta):
    v_orbital = 2 * np.pi * distancia / periodo
    F_gravitacional = G * masa_sol / distancia**2
    print(f"{nombre_planeta}:\nVelocidad orbital: {v_orbital:.2f} m/s")
    print(f"Fuerza gravitacional: {F_gravitacional:.2e} N\n")
    return v_orbital, F_gravitacional

G = 6.67430e-11 
M_sol = 1.989e30

# Marte
r_marte = 2.279e11  # Distancia Marte-Sol en metros
T_marte = 687 * 24 * 60 * 60  # Periodo orbital de Marte en segundos (687 dias)

# Júpiter
r_jupiter = 7.785e11  # Distancia Júpiter-Sol en metros
T_jupiter = 4331 * 24 * 60 * 60  # Periodo orbital de Júpiter en segundos (4332 dias)

v_marte, F_marte = orbita_planeta(M_sol, r_marte, T_marte, "Marte")
v_jupiter, F_jupiter = orbita_planeta(M_sol, r_jupiter, T_jupiter, "Júpiter")

theta = np.linspace(0, 2 * np.pi, 100)
x_marte = r_marte * np.cos(theta)
y_marte = r_marte * np.sin(theta)
x_jupiter = r_jupiter * np.cos(theta)
y_jupiter = r_jupiter * np.sin(theta)

plt.plot(x_marte, y_marte, label='Órbita de Marte')
plt.plot(x_jupiter, y_jupiter, label='Órbita de Júpiter')
plt.scatter(0, 0, color='orange', label='Sol')
plt.xlabel('Posición en x metros')
plt.ylabel('Posición en y metros')
plt.title('Órbitas de Marte y Júpiter alrededor del Sol')
plt.legend()
plt.gca().set_aspect('equal')
plt.show()
