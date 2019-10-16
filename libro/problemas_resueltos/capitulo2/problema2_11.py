CLAVE=int(input("Ingrese la clave de la zona geográfica de la llamada: "))
NUMIN=int(input("Ingrese el número de minutos de la llamada: "))
if CLAVE==12:
    COST=NUMIN*2
if CLAVE==15:
    COST=NUMIN*2.2
if CLAVE==18:
    COST=NUMIN*4.5
if CLAVE==19:
    COST=NUMIN*3.5
if CLAVE==23 or 25:
    COST=NUMIN*6
if CLAVE==29:
    COST=NUMIN*5
print("El costo total de la llamada es de: ", COST)
print("Fin del programa")
