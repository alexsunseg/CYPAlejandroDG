CATE=int(input("Ingrese la categoria del trabajador (1-4):"))
SUE=float(input("Ingrese el sueldo del trabajador:"))
NSUE=0
if CATE==1:
    NSUE=SUE*1.15
elif CATE==2:
    NSUE=SUE*1.10
elif CATE==3:
    NSUE=SUE*1.08
elif CATE==4:
    NSUE=SUE*1.07
print(f"La categoria del trabajador es {CATE} por lo que su nuevo sueldo es de: ${NSUE}")
print("Fin del programa")
