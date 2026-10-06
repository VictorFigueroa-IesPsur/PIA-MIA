#E2.3 · Agenda: diccionario de contactos con alta, baja, búsqueda y listado ordenado, en un bucle de menú.
Agenda={"Angela":"612334565","Pepe":"62345657","Jose":"677759231"}

opcion = 0
while opcion != 5:
    print("")
    print("====== AGENDA ======")
    print("")
    print("1 - Dar de alta un contacto")
    print("2 - Dar de Baja un contacto")
    print("3 - Busca un contacto")
    print("4 - Listado Ordenado")
    print("5 - salir")
    opcion = int(input("Que opción necesita : "))

    if opcion == 1:
        n=str(input("Indique el nombre del contacto: "))
        t=str(input("Indique el numero de telefono del contacto:"))
        Agenda.update({n:t})
        print("Contacto añadido")
        print (Agenda)
        input("Haga click para continuar...")
        continue

    if opcion == 2:
            n=str(input("Indique el nombre del contacto: "))
            Agenda.pop(n)
            print("Contacto Borrado")
            print(Agenda)
            input("Haga click para continuar...")
            continue
    if opcion == 3:
            n=str(input("Indique el nombre del contacto: "))
            print("tlf: "+Agenda[n])
            input("Haga click para continuar...")
            continue
