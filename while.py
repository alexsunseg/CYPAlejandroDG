otra= bool(int(input("Hay más alumnos? (0 NO, 1 SI):")))
suma= 0.0
cont=0
while(otra == True):
    cal= float(input("Calificación:"))
    cont +=1
    suma += cal
    otra=bool(int(input("Hay más alumnos? (0 NO, 1 SI):")))
print("Suma",suma)
print("Promedio",suma/cont)
print("Fin del programa")
