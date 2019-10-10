A=int(input("Ingrese un número entero positivo:"))
B=int(input("Ingrese otro valor entero positivo:"))
C=int(input("Ingrese un ultimo valor entero positivo:"))
if A>B:
    if A>C:
        print(f"A es el valor mayor {A}")
    elif A==C:
        print(f"A y C son mayores {A} y {C}")
    else:
        print(f"C es el mayor {C}")
elif A==B:
    if A>C:
        print(f"A y B son mayores {A} y {B}")
    elif A==C:
        print(f"A, B y C son iguales {A}, {B} y {C}")
    else:
        print(f"C es el mayor {C}")
elif B>C:
        print(f"B es el mayor {B}")
else:
    if B==C:
            print(f"B y C son mayores {B} y {C}")
    else:
            print(f"C es el mayor {C}")
print("Fin del programa")
