SUMPAR=0
SUMIMP=0
CUEPAR=0
I=1
while(I<=270):
    NUM=int(input("Ingrese un número entero: "))
    if NUM<0 or NUM>0:
        if ((-1)**NUM)>0:
            SUMPAR+=NUM
            CUEPAR+=1
        else:
            SUMIMP=SUMIMP+NUM
    I=I+1
PROPAR=SUMPAR/CUEPAR
print(f"El promedio de los números pares ingresados es de {PROPAR} y la suma total de los números impares es de {SUMIMP}")

