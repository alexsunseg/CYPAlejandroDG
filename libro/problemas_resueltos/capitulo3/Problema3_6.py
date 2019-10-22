MAY=-100000
MEN=100000
N=int(input("Ingrese un número entero: "))
I=1
for v in range(0,N,I):
    NUM=int(input("Ingrese otro nùmero entero: "))
    if NUM > MAY:
        MAY=NUM
    if NUM<MEN:
        MEN=NUM
    I+=1
print(f"El número mayor es {MAY} y el menor es {MEN}")
