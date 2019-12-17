# Julio González
# Clase 03
# Las funciones se ponen al inicio del código


def calcular_imc(p,e):
    
    imc=round(p/pow(e,2))
    return imc
def tabla_imc(sexo,imc):
    if sexo == "female":
        if imc < 16:
            dimc = "desnutrido"
        elif imc >= 17 and imc <=20:
            dimc = "bajo de peso"
        elif imc >= 21 and imc <=24:
            dimc = "peso normal"
        elif imc >= 25 and imc <=29:
            dimc = "sobre peso"
        elif imc >= 30 and imc <=34:
            dimc = "obesidad"
        elif imc >= 35 and imc <=39:
            dimc = "obesidad moderada"
        elif imc >= 40:
            dimc = "obesidad morbida"

    if sexo == "male":
        if imc < 17:
            dimc = "desnutrido"
        elif imc >= 18 and imc <=20:
            dimc = "bajo de peso"
        elif imc >= 21 and imc <=25:
            dimc = "peso normal"
        elif imc >= 26 and imc <=30:
            dimc = "sobre peso"
        elif imc >= 31 and imc <=35:
            dimc = "obesidad"
        elif imc >= 36 and imc <=40:
            dimc = "obesidad moderada"
        elif imc >= 41:
            dimc = "obesidad morbida"     
    return dimc

continuar=True

while (continuar==True):
    peso_correcto=False
    estatura_correcta= False  
    print("\t\tIndique su masa corporal")
    
    sexo = input("Ingrese sexo female/male: ")
    #estatura = float(input("Ingrese estatura: "))
    #peso = int(input("Ingrese peso: "))

    while not peso_correcto:
        entrada = input("Indique el peso: ")
        try:
            peso = int(entrada)
            if (peso >= 20 and peso <350):
                peso_correcto=True
            else:
                print("el peso debe estar entre 20 y 350")
        except ValueError:
             print("El peso debe ser un numero entero")
    while not estatura_correcta:
        entrada = input("Indique estatura: ")
        try:
            estatura = float(entrada)
            if (estatura >= 0.5 and estatura <=2.5):
                estatura_correcta=True
            else:
                print("la estatura debe ser entre 0.5 y 2.5")
        except ValueError:
             print("la estatura debe ser un decimal")
             
    imc = calcular_imc(peso, estatura)
    dimc = tabla_imc(sexo,imc)
    print(dimc)
    print("El Imc es: ",imc)
    

    resp=input("Desea otro calculo si/no: ")
    if resp=="no":
       
        continuar=False
    
 
print("Fin")
