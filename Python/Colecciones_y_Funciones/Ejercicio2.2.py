#E2.2 · Deduplicar conservando el orden de aparición original. Es decir, elimina las copias repetidas de una lista.

lista = [2,35,7,7,3,2,1,5,77,9,4,3,98,94,2,2,2,8,56,9,0,11,1,1,2,6,7,8]

print(lista)

n=int(input("Que numero quieres Deduplicar: "))

while lista.count(n) > 1:
    lista.remove(n)

print(lista)

