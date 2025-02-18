# Pedir los valores al usuario
x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))
z = int(input("Ingresa el valor de z: "))
n = int(input("Ingresa el valor de n: "))

# Generar la lista de coordenadas
coordenadas = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n]

# Imprimir la lista
print(coordenadas)