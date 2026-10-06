# Víctor Daniel Rodriguez Figueroa
#E1.1 · Conversor de unidades: pide grados Celsius y muestra Fahrenheit y Kelvin con 2 decimales.

from numpy import rint


c= float(input("Indique la temperatura en Grados Celsius (º): "))

f = c * 9 / 5 + 32
k = c + 273.15

print(f"{c:.2f} C es: {f:.2f} F")
print(f"{c:.2f} C  es: {k:.2f} K")