A=float(input("Ingrese el coeficiente A:"))
B=float(input("Ingrese el coeficiente B:"))
C=float(input("Ingrese el valor de C:"))
DIS=float((B**2)-4*A*C)
if DIS >=0:
    X1=((-B)+DIS**0.5)/(2*A)
    X2=((-B)-DIS**0.5)/(2*A)
    print(f"Las raíces reales son {X1} y {X2}")
print("Fin del programa")
