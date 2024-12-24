import numpy as np
from scipy.optimize import minimize
from scipy.special import gamma, kv
import time

def reconstruir_espectro(Eo, dE, Ef, Energia, um, de, T, max_iter=200):
    start_time = time.time()

    El = np.log10(Energia)
    uml = np.log10(um)
    coefs = np.polyfit(El, uml, 5)

    def funcion_objetivo(params):
        a, b, v, r = params
        if a <= 0 or b <= 0 or a == b or v <= 0 or r < 0 or r > 1:
            return np.inf

        d = 2.7 * 0.1 * de
        um0 = 10 ** np.polyval(coefs, np.log10(Ef))
        try:
            T_model = (
                r * (((a * b) / ((d + a) * (d + b))) ** v) * np.exp(-um0 * d) +
                (1 - r) * (0.2880 * np.exp(-0.2897 * d) +
                           0.5000 * np.exp(-0.2807 * d) +
                           0.1690 * np.exp(-0.2417 * d) +
                           0.0430 * np.exp(-0.2342 * d))
            )
            return np.linalg.norm(T - T_model) ** 2
        except:
            return np.inf

    bounds = [(1e-3, 10), (1e-3, 10), (1e-3, 1), (0, 1)]
    inicial = np.random.rand(4)

    resultado = minimize(funcion_objetivo, inicial, bounds=bounds, options={'maxiter': max_iter})
    a, b, v, r = resultado.x

    E = np.arange(Eo, Ef + dE, dE)
    um_values = 10 ** np.polyval(coefs, np.log10(E))
    um0 = 10 ** np.polyval(coefs, np.log10(Ef))
    dUmdE = np.gradient(um_values, dE)
    with np.errstate(divide='ignore', invalid='ignore'):
        Fb = np.where(
            (um_values > um0) & (a != b) & (v > 0),
            r * (np.sqrt(np.pi) * (a * b) ** 2 / gamma(v)) *
            (((um_values - um0) / (a - b)) ** (v - 0.5)) *
            np.exp(-0.5 * (a + b) * (um_values - um0)) *
            kv(v - 0.5, 0.5 * (a - b) * (um_values - um0)) *
            (-dUmdE),
            0
        )
    Fc = (1 - r) * (0.2880 * np.isclose(E, 58) + 0.5000 * np.isclose(E, 59.5) +
                    0.1690 * np.isclose(E, 67.0) + 0.0430 * np.isclose(E, 69.0))
    F = Fb + Fc
    if np.max(F) > 0:
        F = F / np.max(F)
    else:
        F = np.zeros_like(F)

    K0 = np.sum(F * np.exp(-um_values * 0) * dE)
    K1 = np.sum(F * np.exp(-um_values * 0.58) * dE)
    K2 = np.sum(F * np.exp(-um_values * 0.74) * dE)

    if K0 > 0 and K1 > 0 and K2 > 0 and K2 != K1:
        CSR = (0.58 * np.log(2 * K2 / K0) - 0.74 * np.log(2 * K1 / K0)) / np.log(K2 / K1)
    else:
        CSR = np.nan

    d = 2.7 * 0.1 * de
    T_model_final = (
        r * (((a * b) / ((d + a) * (d + b))) ** v) * np.exp(-um0 * d) +
        (1 - r) * (0.2880 * np.exp(-0.2897 * d) +
                   0.5000 * np.exp(-0.2807 * d) +
                   0.1690 * np.exp(-0.2417 * d) +
                   0.0430 * np.exp(-0.2342 * d))
    )
    error_relativo = np.abs((T - T_model_final) / T).mean() * 100

    tiempo_total = time.time() - start_time

    print("Resultados del ajuste:")
    print(f"Parámetros: a={a:.3f}, b={b:.3f}, v={v:.3f}, r={r:.3f}")
    print(f"CSR (cm²/g): {CSR if not np.isnan(CSR) else 'Incalculable'}")
    print(f"Error relativo promedio: {error_relativo:.2f}%")
    print(f"Tiempo de ejecución: {tiempo_total:.2f} segundos")

    return E, F, CSR, error_relativo

Eo = 20
dE = 1
Ef = 120
Energia = np.linspace(20, 120, 100)
um = np.exp(-Energia / 50)
de = np.linspace(0.1, 0.5, len(Energia))
T = np.exp(-de)

E, F, CSR, error_relativo = reconstruir_espectro(Eo, dE, Ef, Energia, um, de, T)

import matplotlib.pyplot as plt
plt.plot(E, F, label='Espectro reconstruido')
plt.xlabel('Energía (keV)')
plt.ylabel('Espectro Normalizado')
plt.title('Reconstrucción del Espectro de Energía')
plt.legend()
plt.show()
