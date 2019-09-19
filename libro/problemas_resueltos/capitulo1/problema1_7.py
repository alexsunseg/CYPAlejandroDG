L1=float(input("Ingrese el lado 1 del triangulo:"))
L2=float(input("Ingrese el lado 2 del triangulo:"))
L3=float(input("Ingrese el lado 3 del triangulo:"))
S=(L1+L2+L3)/2
AREA=(S*(S-L1)*(S-L2)*(S-L3))**0.5
print("El area del triangulo es igual a:",AREA)
