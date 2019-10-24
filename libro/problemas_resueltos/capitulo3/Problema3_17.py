I=3
SP=0
M=int(input("Ingrese un número: "))
if M>=1:
    SP+=1
    print("Número primo: 1")
    if M>2:
        SP+=1
        print("Número primo: 2")
while (I<=M):
    BAND="V"
    J=3
    while (J<(I//2)) and (BAND="V"):
        if (I%J)=0:
            BAND="F"
        J+=2
    if (BAND="V"):
        print("Número primo: ",I)
        SP+=1
    I+=1
print(f"Entre 1 y el número ingresado hay {SP} números primos")
