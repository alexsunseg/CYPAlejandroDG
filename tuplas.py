#se declaran con "(" y ")"
#son inmutables y organizan datos igual que laslistas
datos_db=('132.248.173.88','root','12345678')
print(datos_db[1])

datos_db=('132.248.173.88','admin','12345678')
print(datos_db[1])
print(datos_db.index('admin'))
print(datos_db.count('12345678'))
