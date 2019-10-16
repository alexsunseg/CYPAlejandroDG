MAT=int(input("Ingrese la matricula del alumno:"))
CAL1=float(input("Ingrese la primer calificación:"))
CAL2=float(input("Ingrese la segunda calificación:"))
CAL3=float(input("Ingrese la tercera calificación:"))
CAL4=float(input("Ingrese la cuarta calificación:"))
CAL5=float(input("Ingrese la quinta calificación:"))
PRO=(CAL1+CAL2+CAL3+CAL4+CAL5)/5
if PRO >= 6:
    print (f"El alumno de matricula {MAT} se encuentra aprobado con un promedio de {PRO}")
else:
    print(f"El alumno de matricula {MAT} se encuentra reprobado con un promedio de {PRO}")
print("Fin del programa")
