SUE=float(input("Ingrese su sueldo actual:"))
if SUE < 1000:
    NSUE= SUE + (SUE*0.15)
    print ("Su nuevo sueldo es de: $", NSUE)
else:
    print ("Su sueldo se mantiene igual")
