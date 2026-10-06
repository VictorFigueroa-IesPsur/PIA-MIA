# Víctor Daniel Rodriguez Figueroa
#E1.2 · Clasificador de notas: pide una nota, valida el rango 0-10 y muestra la calificación.

n= int(input("Ingrese su nota: "))

if n not in range (0,11):
    print("La nota no está en el rango correcto")
else:
    print(n)