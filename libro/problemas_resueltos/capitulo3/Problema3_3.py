SERIE=0
N=int(input("Ingrese un número entero: "))
BAND="T"
I=1
for v in range (0,N,I):
    if BAND=="T":
        SERIE+=(1/I)
        BAND="F"
    else:
        SERIE=SERIE-(1/I)
        BAND="T"
    I+=1
print(SERIE)
