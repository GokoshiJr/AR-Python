# Clase 03 Manejo de listas
salir = False

while not (salir == True):
    print("-"*30)
    print("\tMenu Principal")
    print("-"*30)
    print("1) Cargar valores a la lista")
    print("2) Mostrar Valores")
    print("3) Buscar un elemento")
    print("4) Anexar un elemento al final")
    print("5) Anexar un elemento al principio")
    print("6) Eliminar un elemento")
    print("7) Sustituir elemento")
    print("8) Ordenar Lista")
    print("9) Salir")
    print("-"*30)
    opc = int(input("Seleccione una opción: "))
    print("-"*30)

    if (opc == 1):
        print("1) Cargar valores a la lista")
        print("-"*30)
        numero = int(input("Indique cuantos elementos quiere agregar: "))
        if (numero < 1):
            print("Debe ser mayor que 0")
        else:
            lista = []
        for i in range(numero):
            print("Elemento",str(i+1),": ", end="")
            lista += [input()]
        print (lista)
        print("-"*30)
        espera = input("Presione enter para continuar")
    elif (opc == 2):
        print("2) Mostrar Valores de la Lista")
        print("-"*30)
        for elemento in lista:
            print("", elemento)
        print("-"*30)
        espera = input("Presione enter para continuar")
    elif (opc == 3):
        print("3) Buscar elemento en la lista")
        print("-"*30)
        contador = 0
        buscar = input("Indique el elemento a buscar: ")
        for elemento in lista:
            if elemento == buscar:
                contador += 1
        if contador == 0:
            print("El elemento",buscar,"no aparece en la lista")
        elif contador == 1:
            print("El elemento",buscar,"aparece en la lista")
        else:
            print("El elemento",buscar,"aparece en la lista", contador,"veces")
        print("-"*30)
        espera = input("Presione enter para continuar")
    elif (opc == 4):
        print("4) Anexar elemento al final de la lista")
        print("-"*30)
        lista.append(input("Indique el nombre: "))
        print("La lista queda",lista)
        print("-"*30)
        espera = input("Presione enter para continuar")
    elif (opc == 5):
        print("5) Anexar elemento al principio de la lista")
        print("-"*30)
        lista.insert(0,input("Indique el nombre a anexar: "))
        print("La lista queda",lista)
        print("-"*30)
        espera = input("Presione enter para continuar")
    elif (opc == 6):
        print("6) Elimina un elemento de la lista")
        print("-"*30)
        eliminado = False
        nombre = input("Indique el nombre a eliminar: ")
        for i in range(len(lista)):
            if nombre == lista[i]:
                del(lista[i])
                eliminado = True
                break
        if (eliminado):
            print("Se eliminó",nombre,"de la lista")
            print("La lista queda",lista)
            print("-"*30)
            espera = input("Presione enter para continuar")
        else:
            print("No se encontro",nombre,"en la lista")
            print("-"*30)
            espera = input("Presione enter para continuar")
    elif (opc == 7):
        print("7) Sustituir un elemento de la lista")
        print("-"*30)
        buscar = input("Indique elemento a sustituir: ")
        nombre = input("Indique elemento nuevo: ")
        for i in range(len(lista)):
            if (buscar == lista[i]):
                lista[i]=nombre            
        print("Se eliminó",buscar,"de la lista")
        print("Así quedó la lista:",lista)
        print("-"*30)
        espera = input("Presione enter para continuar")
    elif (opc == 8):
        print("8) Ordenar la lista")
        print("-"*30)
        orden = input("a)Ascendente o b)Descendente: ")
        if (orden == "b"):
            lista.sort(reverse = True)
        else:
            lista.sort()
        print("Lista ordenada")
        print("Así quedó la lista:",lista)
        print("-"*30)
        espera = input("Presione enter para continuar")
    elif (opc == 9):
        salir = True