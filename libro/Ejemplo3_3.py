CUECER=0
N=int(input("Dame un nùmero entero positivo: "))
for i in range (0,N,1):
    NUM=int(input("Ingresa un entero: "))
    if NUM==0:
        CUECER +=1
print("El número de ceros capturados fue:", CUECER)

