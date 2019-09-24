VAR1=float(input("Dame el primer dato:"))
VAR2=float(input("Dame el segundo dato:"))
VAR3=float(input("Dame el tercer dato:"))
if VAR1 > VAR2 and VAR1 > VAR3:
    print (f"El valor {VAR1} es mayor que los otros dos")
if VAR2 > VAR1 and VAR2 > VAR3:
    print(f"El valor {VAR2} es mayor que los otros dos")
if VAR3 > VAR1 and VAR3 > VAR2:
    print(f"El valor {VAR3} es mayor que los otros dos")
print("Fin del programa")
