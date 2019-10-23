NOM=0
SUE=float(input("Ingrese el sueldo del trabajador: "))
while (SUE!=-1):
    if SUE<1000:
        NSUE=SUE*1.15
    else:
        NSUE=SUE*1.12
    NOM+=NSUE
    print("$ ",NSUE)
    SUE=float(input("Ingrese el sueldo del trabajador (De no haber más sueldos ingrese -1): "))
print("El total de la nomina es de: $",NOM)
