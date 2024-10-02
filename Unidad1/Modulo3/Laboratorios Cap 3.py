#3.1.1.4 LABORATORIO: Preguntas y respuestas
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: True o false según cierta sentencia
    Fecha: 23 de septiembre'''
n = int(input("Ingrese un número: "))
print(n >= 100)

#3.1.1.10 LABORATORIO: Operadores de comparación y ejecución condicional
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del if
    Fecha: 23 de septiembre'''
palabra = input("")
if palabra == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
elif palabra == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No " + palabra + "!")

#3.1.1.11 LABORATORIO: Fundamentos de la sentencia if-else
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del if y else
    Fecha: 23 de septiembre'''
income = float(input("Introduce el ingreso anual:"))

if income < 85528:
    tax = income * 0.18 - 556.2
else:
    tax = income - 85528
    tax = tax * 0.32 + 14839

tax = round(tax, 0)
if tax <= 0:
    tax = 0.0
print("El impuesto es:", tax, "pesos")

#3.1.1.12 LABORATORIO: Fundamentos de la sentencia if-elif-else
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del if, elif y else
    Fecha: 23 de septiembre'''
year = int(input("Introduce un año:"))

if year <= 1582:
    print("No está dentro del período del calendario Gregoriano")
elif year % 4 != 0:
    print("Año común")
else:
    print("Año bisiesto")

#3.2.1.3 LABORATORIO: Lo esencial del bucle while - Adivina el número secreto
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del while
    Fecha: 23 de septiembre'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int(input("Introduce el número: "))
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Introduce el número: "))
print("¡Bien hecho, muggle! Eres libre ahora")

#3.2.1.6 LABORATORIO: Fundamentos del bucle for: el conteo
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del for
    Fecha: 23 de septiembre'''
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("¡Listos o no, ahí voy!")

#3.2.1.9 LABORATORIO: La sentencia break - Atascado en un bucle
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del break
    Fecha: 24 de septiembre'''
while True:
    word = input("Ingresa una palabra: ")
    if word == "chupacabra":
        break
print("¡Has dejado el bucle con éxito!")

#3.2.1.10 LABORATORIO: La sentencia continue - El Feo Devorador de Vocales
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del continue
    Fecha: 24 de septiembre'''
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

#3.2.1.11 LABORATORIO: La sentencia continue - El Bonito Devorador de Vocales
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del continue
    Fecha: 24 de septiembre'''
word_without_vowels = ""

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)

#3.2.1.14 LABORATORIO: Fundamentos del bucle while
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del while
    Fecha: 25 de septiembre'''
blocks = int(input("Ingresa el número de bloques: "))

height = 0
bloques_usados = 0

while bloques_usados <= blocks:
    height += 1
    bloques_usados += height
    if bloques_usados > blocks:
        height -= 1
        break

print("La altura de la pirámide:", height)

#3.2.1.15 LABORATORIO: Hipótesis de Collatz
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso del while definido
    Fecha: 26 de septiembre'''
numero = int(input("Ingrese un número entero positivo: "))
pasos = 0

while numero != 1:
    pasos += 1
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
    print(numero)

print("pasos =", pasos)

#3.4.1.6 LABORATORIO: Lo básico de las listas
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso de listas y función .pop
    Fecha: 26 de septiembre'''
hat_list = [1, 2, 3, 4, 5]

numero = int(input("Ingrese un nuevo número: "))
hat_list[2] = numero

hat_list.pop()

print("La longitud de la lista es:", len(hat_list))
print(hat_list)

#3.4.1.13 LABORATORIO: Lo básico de las listas - Los Beatles
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Crear y modificar listas
    Fecha: 26 de septiembre'''
Beatles = []
print("Paso 1:", Beatles)

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]
for miembro in nuevos_miembros:
    Beatles.append(miembro)
print("Paso 3:", Beatles)

Beatles.remove("Stu Sutcliffe")
Beatles.remove("Pete Best")
print("Paso 4:", Beatles)

Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)

print("Los Fav", len(Beatles))

#3.6.1.9 LABORATORIO: Operando con listas - conceptos básicos
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Uso de listas, indexación y operadores in y not in
    Fecha: 26 de septiembre'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

aux = set()
lista = []
for num in my_list:
    if num not in aux:
        aux.add(num)
        lista.append(num)

print("La lista con elementos únicos:")
print(lista)
