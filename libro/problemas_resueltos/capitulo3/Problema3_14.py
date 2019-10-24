AP1=0
AP2=0
AP3=0
AP4=0
AP5=0
RECAU=0
P1=float(input("Ingrese el precio de la localidad 1: "))
P2=float(input("Ingrese el precio de la localidad 2: "))
P3=float(input("Ingrese el precio de la localidad 3: "))
P4=float(input("Ingrese el precio de la localidad 4: "))
P5=float(input("Ingrese el precio de la localidad 5: "))
CLAVE=int(input("Ingrese el tipo de localidad de la venta: "))
CANT=int(input("Ingrese la cantidad de boleto vendidos: "))
while (CLAVE!=(-1)) and (CANT!=(-1)): 
    if CLAVE==1:
        PRE=P1*CANT
        AP1+=CANT
    elif CLAVE==2:
        PRE=P2*CANT
        AP2+=CANT
    elif CLAVE==3:
        PRE=P3*CANT
        AP3+=CANT
    elif CLAVE==4:
        PRE=P4*CANT
        AP4+=CANT
    elif CLAVE==5:
        PRE=P5*CANT
        AP5+=CANT
    print(f"El tipo de localidad es {CLAVE}, la cantidad de boletos vendidos fue de {CANT}, y el precio total de la venta es de: $ {PRE}")
    RECAU+=PRE
    CLAVE=int(input("Ingrese el tipo de localidad de la venta (Para terminar, ingrese -1): "))
    CANT=int(input("Ingrese la cantidad de boleto vendidos (Para terminar, ingrese -1): "))
print("La cantidad de boletos de Tipo 1 vendidos es de ",AP1)
print("La cantidad de boletos de Tipo 2 vendidos es de ",AP2)
print("La cantidad de boletos de Tipo 3 vendidos es de ",AP3)
print("La cantidad de boletos de Tipo 4 vendidos es de ",AP4)
print("La cantidad de boletos de Tipo 5 vendidos es de ",AP5)
print("La recaudación total del estadio es de ", RECAU)
