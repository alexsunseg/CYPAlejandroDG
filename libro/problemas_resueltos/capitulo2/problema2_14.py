TIPOENF=int(input("Ingrese el tipo de enfermedad del paciente (1-4): "))
EDAD=int(input("Ingrese la edad del paciente: "))
DIAS=int(input("Ingrese el número de días que el paciente estuvo hospitalizado: "))
if TIPOENF==1:
    COSTOT=DIAS*25
elif TIPOENF==2:
    COSTOT=DIAS*16
elif TIPOENF==3:
    COSTOT=DIAS*20
elif TIPOENF==4:
    COSTOT=DIAS*32
if EDAD >= 14 and EDAD<=22:
    COSTOT=COSTOT*1.1
print("El costo total de la internación del paciente es de: $",COSTOT)
print("Fin del programa")
