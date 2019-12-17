# Clase 03
salir = False
while not (salir == True):
    print("\t\t Menu Principal")
    print("\t\t 1) Cargar valores a la lista")
    print("\t\t 2) Mostrar Valores")
    print("\t\t 3) Buscar un elemento")
    print("\t\t 4) Anexar un elemento al final")
    print("\t\t 5) Anexar un elemento al principio")
    print("\t\t 6) Eliminar un elemento")
    print("\t\t 7) Sustituir elemento")
    print("\t\t 8) Ordenar Lista")
    print("\t\t 9) Salir")
    opc = int(input("Seleccione una opción "))
    if (opc == 1):
        print("\t\t 1) Cargar valores a la lista")
        numero = int(input("Indique cuantos nombres quiere agregar "))
        if (numero < 1):
            print("Debe ser mayor que 0")
        else:
            lista = []
        for i in range(numero):
            print("\t\t Indique el nombre ", str(i+1), ":", end="")
            lista += [input()]
        print (lista)
        espera = input("Presione enter para continuar")
    elif (opc == 2):
        print("\t\t 2)Mostrar Valores de la Lista")
        for elemento in lista:
            print("", elemento)
        espera = input("Presione enter para continuar")
    elif (opc == 3):
        print("\t\t 3) Buscar un elemento en la lista")
        contador = 0
        buscar = input("indique el nombre")
        for elemento in lista:
            if elemento == buscar:
                contador += 1
        espera = input("Presione enter para continuar")
    elif (opc == 9):
        salir = True
        

            

