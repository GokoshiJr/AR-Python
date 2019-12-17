# Cuentas Bancarias
# Clase 04

seguir = True
movimiento = []
detalle = []
nombre = ""
monto = 0
sw = False    
while seguir:
    print("\t\t Menu Principal")
    print("\t\t 1)Crear Cuentas")
    print("\t\t 2)Deposito")
    print("\t\t 3)Retiro")
    print("\t\t 4)Saldo")
    print("\t\t 5)Ver Detalle")
    print("\t\t 6)Salir")

    opc = input("\t\t Seleccione una Opción: ")
       

    if opc == "1":
        print("Crear Cuentas")
        respuesta = False
        while not respuesta:
            nombre = input("Indique su nombre: ")
            monto = int(input("Indique el monto de apertura: "))
            r = input("Datos Correctos s/n ")
            if (r == "s" or r == "S"):
                respuesta = True
                sw = True
                movimiento.append (monto)
                detalle.append ("Monto de apertura")
                
                
        espera = input("Presione enter para continuar")
            
        
    elif opc == "2":
        if sw == True:
            print("Deposito")
            respuesta = False
            while not respuesta:
                deposito = int(input("Indique el deposito: "))
                r = input("Monto Correcto s/n ")
                if (r == "s" or r == "S"):
                    respuesta = True
                    detalle.append ("Deposito")
                    movimiento.append (deposito)
                    monto = monto+deposito
        else:
            print("Debes crear una cuenta")
        espera = input("Presione enter para continuar")
        
    elif opc == "3":
        if sw:
            print("Retiro")
            respuesta = False
            while not respuesta:
                retiro = int(input("Indique el retiro: "))
                r = input("Monto Correcto s/n ")
                if (r == "s" or r == "S"):
                    respuesta = True
                    detalle.append ("Retiro")
                    movimiento.append (retiro)
                    monto = monto-reversed
        else:
            print("Debes crear una cuenta")
        espera = input("Presione enter para continuar")
        
    elif opc == "4":
        if sw:
            print("Saldo Actual")
            print ("Nombre ", nombre)
            print ("Saldo", monto)
        else:
            print("Debes crear una cuenta")
        espera = input("Presione enter para continuar")
        
    elif opc == "5":
        if sw:            
            print("Ver Detalle")
            print ("---------------------------------")
            print ("Detalle del Movimiento:")
            print ("---------------------------------")
            print ("Nombre:", nombre)
            print ("---------------------------------")
            for i in range (len(movimiento)):
                print("{0:<20}{1:>10}".format(detalle[i], movimiento[i]))
            print ("---------------------------------")
            print("{0:<20}{1:>10}".format("Saldo actual:", monto))
            print ("---------------------------------")
        else:
            print("Debes crear una cuenta")
        espera = input("Presione enter para continuar")
        
    elif opc == "6":
        print("Salir")
        espera = input("Presione enter para continuar")
        seguir = False
        
    else:
        print("Debe seleccionar una opción valida")
        espera = input("Presione enter para continuar")
    
