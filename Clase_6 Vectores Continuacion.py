# Clase 6 Vectores

def menuPrincipal():
    print("\t\t       Menu Principal")
    print("\t\t 1) Carga Manual")
    print("\t\t 2) Carga Automática")
    print("\t\t 3) Mostrar Vector")
    print("\t\t 4) Número más Alto y más Bajo")
    print("\t\t 5) Sumatoria pares impares")
    print("\t\t 6) Buscar un Número")
    print("\t\t 7) Mostrar los Número Primos")
    print("\t\t 8) Ordenar el Vector")
    print("\t\t 9) Salir")
    
    opc = input("\t\t Seleccione una Opción: ")
    return opc

def cargaManual():
    print("")
    print("\t\t Carga manual")
    for i in range(len(vector)):
        print("Indique el valor del vector en la posicion", i+1, ":", end=" ")
        vector[i] = input()        
    espera = input("Presione Enter para continuar ")

def cargaAutomatica():
    print("")
    print("\t\t Carga Automática")
    for i in range (len(vector)):
        vector[i] = randrange(1, 99)
        print("\t\t Vector Posicion", i+1, ":", vector[i])
    espera = input("\t\t Presione Enter para continuar")

def mostrarVector():
    print("")
    print("\t\t Mostrar el Vector")
    for i in range (len(vector)):
        print("\t\t vector", i+1,":", vector[i])
    espera = input("Presione Enter para continuar")

def numeroAlto():
    print("")
    print("\t\t Mostrar el Número más alto y el más bajo")
    vmax = 0
    vmin = 0    
    for i in range (len(vector)):
        if i == 0:
            vmax = vector[i]
            vmin = vector[i]
        if (vector[i] > vmax):
            vmax = vector[i]
        if (vector[i] < vmin):
            vmin = vector[i]
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
    for i in range (len(vector)):         
        total = total + vector[i]
        if (vector[i]%2 == 0):
            n = "Es Par"
            cp = cp + 1
            sp = sp + vector[i]
        else:
            n = "Es Impar"
            ci = ci + 1
            si = si + vector[i]
        print (vector[i],n)

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
    for i in range(len(vector)):
        if (n == vector[i]):
            p = i
    if (p == ""):
        print("El número", n , "No se encuentra en el Vector")
    else:
        print("El número", n , "Si se encuentra en el Vector")                           
    espera = input("Presione Enter para continuar")

def mostrarPrimos():
    print("")
    print("\tNúmeros Primos:")
    print("-----------------------------------")
    for i in range(len(vector)):        
        divisible = 0
        for h in range(1 , vector[i]+1):            
            if(vector[i]%h == 0):
                divisible = divisible + 1
        n = ""
        if(divisible == 2):
            n = "Es primo"                        
            print(vector[i],"", n)                
    espera = input("Presione Enter para continuar")

def ordenarVector():
    print("") # ordenamiento modo burbuja con 2 for y una variable auxiliar    
    print("\tOrdenar Vector")
    for i in range(len(vector)):
        for j in range(i, len(vector)):
            if (vector[i] > vector[j]):
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux
    print(vector)                                
    espera = input("Presione Enter para continuar")



def opciones(opc):
    salir = False
    if (opc == "1"):
        cargaManual()        
    elif (opc == "2"):
        cargaAutomatica()             
    elif (opc == "3"):
        mostrarVector()      
    elif (opc == "4"):
        numeroAlto()            
    elif (opc == "5"):
        sumatoria()                
    elif (opc == "6"):
        buscarNum()        
    elif (opc == "7"):
        mostrarPrimos()        
    elif (opc == "8"):
        ordenarVector()        
    elif (opc == "9"):
        salir = True
    else:
        print("Seleccione una Opción Valida")

    return salir
    
    

    
import os, sys
from random import randrange
vector = [10, 47, 53, 25, 60, 41,7, 12, 85, 10]
salir = False

while not salir:
    opc = menuPrincipal()
    salir = opciones(opc)
    
    



