SUE=float(input("Ingrese su sueldo actual:"))
if SUE < 1000:
    NSUE= SUE + (SUE*0.15)
    print("Su nuevo sueldo es de: $", NSUE)
else: 
    NSUE= SUE + (SUE*0.12)
    print("Su nuevo sueldo es de: $", NSUE)
