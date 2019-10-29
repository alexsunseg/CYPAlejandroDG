#escritura
frutas=["Zapote","Manzana","Pera","Aguacate","Durazno","Uva","Sandia"]
#lectura, el selector [indice]
print(frutas[2])
print("-------")
#lectura con for 
#opción 1
for indice in range (0,7,1):
    print(frutas[indice])
print("-------")
#for opción 2--por un iterador for each, solo funciona con arreglos
for fr in frutas:
    print(fr)
print("-------")
#asignación
frutas [2]="Melon"
print(frutas)
print("-------")
#inserción al final, append agrega más miembros a la lista
frutas.append("Naranja")
print(frutas)
print(len(frutas))
print("-------")
frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))
print("-------")
frutas.insert(0,"Mamey")
print(frutas)
print("-------")
#eliminación con pop, elimina el ultimo
print(frutas.pop())
print(frutas)
print("-------")
print(frutas.pop(1))
print(frutas)
#eliminación con remove, busca de inicio a fin 
frutas.append("Limon")
frutas.append("Limon")
print(frutas)
frutas.remove("Limon")
print(frutas)
#ordenamiento
print("-------")
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
print("-------")
#busqueda
print(f"La Uva está en la posición: {frutas.index('Uva')}")
#count
print(f"El limon está {frutas.count('Limon')} veces en la lista")
#extend, une dos listas, una al final de la otra
print("-------")
print(frutas)
otras_frutas=["Rambutan","Nispero","Liche","Pitahaya"]
frutas.extend(otras_frutas)
print(frutas)
print("-------")
#copiar, de esta manera se modifican ambos
copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)
print("-------")
#copia con copy
otra_copia=frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)
