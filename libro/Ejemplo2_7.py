NUM = int(input("Ingresa un numero entero positivo:"))
V= int(input("Ingresa otro nùmero entero positivo:"))
VAL=0
if NUM==1:
    VAL=100*V
elif NUM==2:
    VAL=100**V
elif NUM==3:
    VAL=100/V
else:
    VAL=0
print(f"El resultado es {VAL}")
print("Fin del programa")
