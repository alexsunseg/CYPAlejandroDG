NUM=float(input("Ingrese el valor del monto: "))
if NUM<500:
    print("Pagar monto ingresado")
elif NUM<=1000:
    DES= NUM-NUM*0.05
    print(f"Pagar nuevo monto con 5% de descuento: ${DES}")
elif NUM<=7000:
    DES= NUM-NUM*0.11
    print(f"Pagar nuevo monto con 11% de descuento: ${DES}")
elif NUM<= 15000:
    DES=NUM-NUM*0.18
    print(f"Pagar nuevo monto con 18% de descuento: ${DES}")
else:
    DES=NUM-NUM*0.25
    print (f"Pagar nuevo monto con 25% de descuento: ${DES}")
print("Fin del programa")
