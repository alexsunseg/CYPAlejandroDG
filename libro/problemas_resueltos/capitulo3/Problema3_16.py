
TIPO1=0
TIPO2=0
TIPO3=0
TIPO4=0
TIPO5=0
MCTIPO2=0
N=int(input("Ingrese el numero de años a revisar: "))
I=1
for v in range (0,N,I):
    TOTVIN=0
    J=1
    for i in range (0,5,J):
        V=float(input("Ingrese la cantidad de vino en litros: "))
        TOTVIN+=V
        if J == 1:
            TIPO1+=V
        elif J==2:
            TIPO2+=V
        if V>MCTIPO2:
            MCTIPO2=V
            AÑO=1
        TIPO3+=V
        if V=0:
            print(f"En el año {I} no se produjo vino TIPO3")
        TIPO4+=V
        TIPO5+=V
        J+=1
    print("El total de litros producidos por año es de: ",TOTVIN)
    I+=1
print("El total del Tipo 1 es de: ", TIPO1)
print("El total del Tipo 2 es de: ", TIPO2)
print("El total del Tipo 3 es de: ", TIPO3)
print("El total del Tipo 4 es de: ", TIPO4)
print("El total del Tipo 5 es de: ", TIPO5)
print(f"El año en que se produjo mayor cantidad de vino Tipo 2 es {AÑO}, el total de litros es de {MCTIPO2}")
