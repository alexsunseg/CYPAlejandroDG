ARNO=0
ARCE=0
ARSU=0
MERSU=500000
I=1
for v in range (1,13,I):
    RNO=float(input("Ingrese la cantidad de lluvia caída en la región norte: "))
    RCE=float(input("Ingrese la cantidad de lluvia caída en la región centro: "))
    RSU=float(input("Ingrese la cantidad de lluvia caída en la región sur: "))
    ARNO+=RNO
    ARCE+=RCE
    ARSU+=RSU
    if RSU<MERSU:
        MERSU=RSU
        MES=I
    I+=1
PRORCE=ARCE/12
print("El promedio anual de la región centro es de: ", PRORCE)
print("El mes con menor lluvia en la zona sur es el: ", MES)
print("El registro del mes con menor lluvia de la región sur es de: ",MERSU)
if ARNO>ARCE:
    if ARNO>ARSU:
        print("La región con mayor lluvias es la norte")
    else:
        print("La región con mayor lluvias es la sur")
else:
    if ARCE>ARSU:
        print("La región con mayor lluvias es la centro")
    else:
        print("La región con mayor lluvias es la sur")
print("Fin del programa")

