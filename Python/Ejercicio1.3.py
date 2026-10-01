# Víctor Daniel Rodriguez Figueroa
#E1.3 · Tabla de multiplicar con formato alineado usando f-strings.

t= int(input("Que tabla de multiplicar necesitas: "))
print("================================================")
for i in range(1,11):
    resultado= t* i
    print(f"{t:^2} x {i:>3} = {resultado}")
    