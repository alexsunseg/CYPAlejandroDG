MAT=int(input("Ingrese la matrícula del alumno: "))
CARR=input("Ingrese la carrera a la que esté inscrito el alumno (Economía-Computación-Administración-Contabilidad): ")
SEM= int(input("Ingrese el semestre aprobado por el alumno: "))
PROM= float(input("Ingrese el promedio del alumno: "))
if CARR== "Economía":
    if SEM >=6 and PROM>=8.8:
        print(f"El alumno de matrícula {MAT} de la carrera en {CARR} es aceptado")
elif CARR== "Computación":
    if SEM>6 and PROM>8.5:
         print(f"El alumno de matrícula {MAT} de la carrera en {CARR} es aceptado")
elif CARR== "Administración" or "Contabilidad":
    if SEM>5 and PROM>8.5:
         print(f"El alumno de matrícula {MAT} de la carrera en {CARR} es aceptado")
print("Fin del programa")
