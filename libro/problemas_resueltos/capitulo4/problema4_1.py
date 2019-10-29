N=int(input("Ingrese el número de elementos del arreglo: "))
VEC= []
if N >= 1 and N <= 500:
    #logica
    for I in range (0,N,1):
        VEC.append(int(input("Ingresa valor: ")))
    VEC.sort()
    print(VEC)
    print("Lista de números sin repeticiones: ")
    I=0
    while I<=N-1:
        print(VEC[I])
        REPET=VEC[I]
        while I<=N-1 and REPET==VEC[I]:
            I+=1
else:
    print("El número de elementos del arreglo es incorrecto")
