N=int(input("Ingrese un número: "))
I=1
for v in range (0,N,I):
    SUM=0
    J=1
    for i in range (1,(I//2),J):
        if (I%J)==0:
            SUM+=J
        J+=1
    if SUM==J: 
        print(I, "Es un número perfecto")
    I+=1
