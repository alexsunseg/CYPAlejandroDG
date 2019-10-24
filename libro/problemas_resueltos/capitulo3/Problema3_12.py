MASUE=0
N=int(input("Ingrese el número de empleados de la empresa: "))
I=1
for v in range (0,N,I):
    NUMEMP=int(input("Ingrese el número del empleado: "))
    SUE=float(input("Ingrese el sueldo del empleado: $ "))
    if SUE>MASUE:
        MASUE=SUE
        MANUM=NUMEMP
    I=1
print(f"El empleado de número {MANUM} tiene el mayor sueldo de ${MASUE}")
