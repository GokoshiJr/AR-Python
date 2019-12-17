# NOTAS

notas = open("NotasParciales_0.txt")
reporte = open("Reporte.txt","w")
print("\t\t\t     Listado de Alumnos")
print("-"*90)
print("{0:<15}""{1:5}""{2:>10}""{3:>10}""{4:>10}""{5:>15}""{6:>15}". format("Nombre","Sexo","Nota1","Nota2","Nota3","Promedio","Estatus"))
print("-"*90)
A = 0
R = 0
for linea in notas:
    columna = linea.strip().split(":")
    nombres = columna[0]
    sexo = columna[1]
    nota1 = int(columna[2])
    nota2 = int(columna[3])
    nota3 = int(columna[4])
    promedio =((nota1 + nota2 + nota3)/3)

    if (promedio >= 10):
        estatus = "Aprobado"
        A+=1
    else:
        estatus = "Reprobado"
        R+=1

       
    
    print("{0:<15}""{1:5}""{2:>10}""{3:>10}""{4:>10}""{5:>15.2f}""{6:>15}". format(nombres,sexo,nota1,nota2,nota3,promedio,estatus))

    
print("Cantidad de Aprobados",A)
print("Cantidad de Reprobados",R)
