SUMPOS=0
CUEPOS=0
SUMOTR=0
N=int(input("Ingrese un número entero: "))
I=1
for v in range (0,N,I):
    NUM=int(input("Ingrese un número entero: "))
    if NUM>0:
        SUMPOS+=NUM
        CUEPOS+=1
    else:
        SUMOTR+=NUM
    I+=1
PROGEN=(SUMPOS+SUMOTR)/N
PROPOS=SUMPOS/CUEPOS
print(f"El total de números positivos es de {CUEPOS}, el promedio de los números positivos es de {PROPOS}, el promedio general de los números es de {PROGEN}")
