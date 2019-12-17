# Clase 07 Matrices

def menuPrincipal():
    print("")
    print("\t\t    Menu Principal")
    print("")    
    print("\t\t 1) Carga Manual")
    print("\t\t 2) Carga Automática")
    print("\t\t 3) Mostrar Matriz")
    print("\t\t 4) Número más Alto y más Bajo")
    print("\t\t 5) Sumatoria pares impares")
    print("\t\t 6) Buscar un Número")
    print("\t\t 7) Mostrar los Número Primos")
    print("\t\t 8) Ordenar La matriz")
    print("\t\t 9) Mostrar Diagonal Principal")
    print("\t\t 10) Salir")
    
    opc = input("\t\t Seleccione una Opción: ")
    return opc

def cargaManual():
    print("")
    print("\t\t Carga manual")
    for i in range(10):
        for j in range (10):
            matriz[i][j] = int(input("Indique el numero "))        
    espera = input("Presione Enter para continuar ")

def cargaAutomatica():
    print("")
    print("\t\t Carga Automática")
    for i in range (10):
        for j in range (10):
            matriz[i][j] = randrange(10, 99)
    mostrarMatriz()
    
def mostrarMatriz():
    print("")
    print("\t\t Mostrar la matriz")
    for i in range (10):
        for j in range (10):
            print("[",matriz [i] [j],"]", end="")
        print(" ")
    print(" ")
    espera = input("Presione Enter para continuar")

def numeroAlto():
    mostrarMatriz()
    print("")
    print("\t\t Mostrar el Número más alto y el más bajo")
    vmax = 0
    vmin = 0    
    for i in range (10):
        for j in range (10):
            if i == 0:
                vmax = matriz[i][j]
                vmin = matriz[i][j]
            if (matriz[i][j] > vmax):
                vmax = matriz[i][j]
            if (matriz[i][j] < vmin):
                vmin = matriz[i][j]
    print("El Número más bajo del vector es: ", vmin)
    print("El Número más alto del vector es: ", vmax)        
    espera = input("Presione Enter para continuar")

def sumatoria():
    print("")
    print("Sumatoria de números pares e impares")
    print("--------------------------------------") 
    cp = 0
    ci = 0
    total = 0
    sp = 0
    si = 0
    for i in range (10):
        for j in range (10):
            total = total + matriz[i][j]
            if (matriz[i][j]%2 == 0):
                n = "Es Par"
                cp = cp + 1
                sp = sp + matriz[i][j]
            else:
                n = "Es Impar"
                ci = ci + 1
                si = si + matriz[i][j]
            print (matriz[i][j],n)

    print("--------------------------------------")    
    print("Total: ",total)
    print("Numero pares: ", cp)
    print("Numero impares: ", ci)
    print("Suma de pares: ", sp)
    print("Suma de impares: ", si)
    print("")
    espera = input("Presione Enter para continuar")

def buscarNum():
    print("")    
    print("Buscar número")
    n = int(input("Indique el numero a buscar "))
    p = ""
    r = ""
    for i in range(10):
        for j in range(10):
            if (n == matriz[i][j]):
                p = i
                r = j
    if (p == ""):
            print("El número", n , "No se encuentra en la matriz")
    else:
            print("El número", n , "Si se encuentra en la matriz")
            print("Se encuentra ubicado en la fila", p+1, "Columna", r+1)
    espera = input("Presione Enter para continuar")

def mostrarPrimos():
    print("")
    print("\tNúmeros Primos:")
    print("-----------------------------------")
    for i in range(10):
        for j in range(10): 
            divisible = 0
            for h in range(1 , matriz[i][j]+1):            
                if(matriz[i][j]%h == 0):
                    divisible = divisible + 1
            n = ""
            if(divisible == 2):
                n = "SP"
            else:
                n = "NP"
            print(" [",matriz [i][j],n,"]", end="")                
    espera = input("Presione Enter para continuar")

def ordenarMatriz():
    print("") # ordenamiento modo burbuja con 2 for y una variable auxiliar    
    print("\tOrdenar Vector")
    orden = int(input("\t Indique 1) De mayor a menor 2)De menor a mayor: "))
    if (orden == 1):
        
        for i in range(10):
            for j in range(10):
                for h in range(10):
                    for k in range (10):
                        if (matriz[i][j] > matriz[h][k]):
                            aux = matriz[i][j]
                            matriz[i][j] = matriz[h][k]
                            matriz[h][k] = aux
    if (orden == 2):
        for i in range(10):
            for j in range(10):
                for h in range(10):
                    for k in range (10):
                        if (matriz[i][j] < matriz[h][k]):
                            aux = matriz[i][j]
                            matriz[i][j] = matriz[h][k]
                            matriz[h][k] = aux
    mostrarMatriz()                                
    


def diagonalPrincipal():
    print("")
    print("\t\t         Diagonal Principal")
    print("")
    for i in range (10):
        for j in range (10):
            if (i == j):
                print(" {",matriz [i][j],"}", end="")
            else:
                print(" [",matriz [i][j],"]", end="")
                
    print("")
    print("")
    espera = input("Presione Enter para continuar")
                

    
def opciones(opc):
    salir = False
    if (opc == "1"):
        cargaManual()        
    elif (opc == "2"):
        cargaAutomatica()             
    elif (opc == "3"):
        mostrarMatriz()      
    elif (opc == "4"):
        numeroAlto()            
    elif (opc == "5"):
        sumatoria()                
    elif (opc == "6"):
        buscarNum()        
    elif (opc == "7"):
        mostrarPrimos()        
    elif (opc == "8"):
        ordenarMatriz()        
    elif (opc == "9"):
        diagonalPrincipal()
    elif (opc == "10"):
        salir = True
    else:
        print("Seleccione una Opción Valida")

    return salir
    
    

    
import os, sys
from random import randrange
matriz = ([10]*10, [47]*10, [53]*10, [25]*10, [60]*10, [41]*10, [75]*10, [12]*10, [85]*10, [10]*10)
salir = False

while not salir:
    opc = menuPrincipal()
    salir = opciones(opc)
