def fuerza(masa, aceleracion):
    return masa * aceleracion

masa = float(input("Ingrese la masa (kg): "))
while(masa <= 0):
    masa = float(input("Ingrese una masa válida\nIngrese la masa (kg): "))
aceleracion = float(input("Ingrese la aceleracion (m/s^2): "))
fuerza = fuerza(masa, aceleracion)
print(f"La fuerza es: {fuerza} N")
