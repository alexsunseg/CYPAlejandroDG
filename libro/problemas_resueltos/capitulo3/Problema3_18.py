MAYPRO=0
N=int(input("Ingrese el número de fabricas: "))
if N<=100:
    I=1
    for v in range (0,N,I):
        FABRICA=int(input("Ingrese la clave de la fábrica: "))
        TOTANU=0
        J=1
        for i in range (1,13,J):
            MES=float(input("Ingrese la producción del mes: "))
            TOTANU+=MES
            if J==7 and MES>3000000:
                print("Fabrica con clave ",FABRICA)
            J+=1
        if TOTANU>MAYPRO:
            MAYPRO=TOTANU
            CLAVE=FABRICA
        print(f"La producción anual de la fabrica {FABRICA} es de: $ {TOTANU}")
        I+=1
    print(f"La clave de la fábrica que más produjo en el año es {CLAVE} con una producción de: $ {MAYPRO}")
else:
    print("Error en número de fábricas")

