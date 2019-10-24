SERIE=0
N=int(input("Ingrese un número: "))
I=1
for v in range (0,N,I):
    SERIE+=I**I
    I+=1
print(SERIE)
