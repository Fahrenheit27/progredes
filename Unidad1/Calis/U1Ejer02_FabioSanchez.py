'''
   Nombre: Fabio Alonso Sánchez García
   Grupo: GIR0641
   Descripción: Ejercicio 02 Crear una lista de nombres y realizar operaciones básicas
   Fecha: 03/10/2024
'''

# Crear una lista con cuatro compañeros del grupo
nombres = ["Francisco", "Pedro", "Juan", "Fernando"]

# Desplegar el tamaño de la lista
print("El tamaño de la lista es:", len(nombres))

# Desplegar el contenido de la lista
print("El contenido de la lista es:", nombres)

# Cambiar el segundo elemento de la lista por "Joaquín"
nombres[1] = "Joaquín"

# Agregar un elemento más a la lista con el nombre "Luis Miguel"
nombres.append("Luis Miguel")

# Eliminar el tercer elemento de la lista
del nombres[2]

# Desplegar la lista en orden inverso, separados por un espacio
print("Lista en orden inverso:", " ".join(nombres[::-1]))
