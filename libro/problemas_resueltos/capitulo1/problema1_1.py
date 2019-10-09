PREPRO=float(input("Ingrese el precio del producto:"))
PAGO=float(input("Ingrese el monto de pago:"))
DEVO=PAGO-PREPRO
print(f"Pagaste ${PAGO}, el precio del producto es ${PREPRO} y tu cambio es ${DEVO}")
