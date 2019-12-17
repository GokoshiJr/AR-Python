# Clase 02 
# Cálculos Básicos
# Julio González


def menu():    
    print("\t\tMenu Principal")
    print("\t\t1)Suma")
    print("\t\t2)Resta")
    print("\t\t3)Multiplicación")
    print("\t\t4)División")
    print("\t\t5)Numero Par o Impar")    
    print("\t\t9)Salir")
    opcion=input("Seleccione una Opción 1/2/3/4/5/9:")
    return opcion

def suma():   
    print("Suma")
    n1=int(input("Indique el Número"))
    n2=int(input("Indique el Número"))
    suma=n1+n2 
    print("El resultado es:",suma)     
def resta():
    print("Resta")
    n1=int(input("Indique el Número"))    
    n2=int(input("Indique el Número"))
    resta=n1-n2
    print("El resultado es:",resta) 
def multiplicacion():
    print("Multiplicación")
    n1=int(input("Indique el Número"))    
    n2=int(input("Indique el Número"))
    multiplicacion=n1*n2
    print("El resultado es:",multiplicacion)
def division(): 
    print("División")
    n1=int(input("Indique el Número"))    
    n2=int(input("Indique el Número"))
    division=n1/n2
    print("El resultado es:",division)  
def numeropar():
    print("Numero Par o Impar")
    n=int(input("Indique el Número"))
    if(n%2==0):
        print("el numero:",n,"es par")
    else:
        print("el numero:",n,"es impar")  
salir=False
while not salir: 
    opcion=menu()
    if(opcion=="1"):
        suma()
    elif(opcion=="2"):
        resta()
    elif(opcion=="3"):
        multiplicacion()
    elif(opcion=="4"):
        division()
    elif(opcion=="5"):
        numeropar()    
    elif(opcion=="9"):
     salir=True
    else:
        print("Debe ser un numero del 1 al 5")       
espera=input("presione la tecla para salir")


    
