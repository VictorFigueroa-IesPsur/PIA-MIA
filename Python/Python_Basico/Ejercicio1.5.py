# Victor Daniel Rodriguez Figueroa
#E1.5 · Adivina el número: bucle while con intentos limitados y pistas mayor/menor.

Adivina= 7
intentos= 3
contador= 0
while contador < 3:
    numero = int(input("Adivina el número del 1 al 100: "))
    if numero == Adivina:
        print("Felicidades Adivinaste el número.")
        break
    elif numero < Adivina:
        print("El número es mayor. Intenta de nuevo.")
        contador += 1
    elif numero > Adivina:
        print("El número es menor. Intenta de nuevo.")
        contador += 1

if contador == 3:
    print("Se acabaron los intentos. El número era: ", Adivina)   