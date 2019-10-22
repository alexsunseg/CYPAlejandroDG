CHI=0
MED=0
GRA=0
N=int(input("Ingrese el número de ventas: "))
I=1
for v in range (0,N,I):
    V=float(input("Ingrese el monto de la venta: $ "))
    if V <=200:
        CHI+=1
    elif V<400:
        MED+=1
    else: 
        GRA+=1
    I+=1
print(f"El número de ventas chicas fue de {CHI}, el de medianas fue de {MED} y el de grandes es de {GRA}")
