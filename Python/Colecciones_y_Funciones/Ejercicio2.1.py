#E2.1 · Estadísticas de una lista de notas: media, máximo, mínimo y cuántas aprobadas, sin usar statistics.
notas = [2,3,6,9,1,2,10,8,9,9,5,6,6,7,9,9,8,6]

media = sum(notas) / len(notas)
maximo = max(notas)
minimo = min(notas)
aprobados = 0

for n in notas:
    if n > 5:
        aprobados = aprobados + 1

print("Estadisticas")
print(f"{media:.2f}")
print (maximo)
print (minimo)
print (aprobados)

