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
    print("\t\t Carga manual")
    for i in range(len(vector)):
        print("Indique el valor del vector en la posicion", i+1, ":", end=" ")
        vector[i] = input()        
    espera = input("Presione Enter para continuar ")

def cargaAutomatica():
    print("\t\t Carga Automática")
    for i in range (len(vector)):
        vector[i] = randrange(1, 99)
        print("\t\t Vector Posicion", i+1, ":", vector[i])
    espera = input("Presione Enter para continuar")

def mostrarVector():
    print("\t\t Mostrar el Vector")
    for i in range (len(vector)):
        print("\t\t vector", i+1,":", vector[i])
    espera = input("Presione Enter para continuar")

def numeroAlto():
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
    print("carga manual")
    espera = input("Presione Enter para continuar")

def buscarNum():
    print("carga manual")
    espera = input("Presione Enter para continuar")

def mostrarPrimos():
    print("carga manual")
    espera = input("Presione Enter para continuar")

def ordenarVector():
    print("carga manual")
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
        buscarNum()        
    elif (opc == "8"):
        ordenarVector()        
    elif (opc == "9"):
        salir = True
    else:
        print("Seleccione una Opción Valida")

    return salir
    
    

    
import os, sys
from random import randrange
vector = [10, 15, 3, 25, 60, 41,72, 12, 85, 1000]
salir = False

while not salir:
    opc = menuPrincipal()
    salir = opciones(opc)
    
    



