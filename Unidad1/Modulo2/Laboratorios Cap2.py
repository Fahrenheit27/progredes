#2.1.1.6 LABORATORIO: La función print()
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Utiliza la función print() para imprimir la linea 
    "¡Hola, Mundo!" en la pantalla, utiliza el print en todo momento.
    Fecha: 19 de septiembre'''
print("¡Hola Mundo")
print("Fabio Alonso Sánchez García")
print(Fabio)
print Fabio

#2.1.1.18 LABORATORIO: Dando formato a la salida
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Modifica la primera línea de código en el editor, 
    utilizando las palabras clave sep y end, para que coincida con el resultado esperado.
    Fecha: 19 de septiembre'''
print("Fundamentos", "Programación", "en", sep="***", end="...")
print("Python")
      
#2.1.1.19 LABORATORIO: Dando formato a la salida
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Minimizar el número de invocaciones de la función print() 
    insertando la secuencia \n en las cadenas.
    Fecha: 19 de septiembre'''
print("    *\n","   * *\n","  *   *\n"," *     *\n","***   ***\n","  *   *\n","  *   *\n","  *****")
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)

#2.2.1.11 LABORATORIO: Literales de Python - Cadenas
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Escribe una sola línea de código, utilizando la función print(), 
    así como los caracteres de nueva línea y escape, para obtener la salida esperada de tres líneas.
    Fecha: 19 de septiembre'''
print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")

#2.4.1.7 LABORATORIO: Variables
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, 
    y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). 
    Fecha: 19 de septiembre'''
juan=3
maria=5
adan=6
juan=int(juan)
maria=int(maria)
adan=int(adan)
print(juan,",",+maria,",",+adan)
total_manzanas=juan+maria+adan
print(total_manzanas)

#2.4.1.9 LABORATORIO: Variables, un sencillo convertidor
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Su trabajo es redondear la salida del resultado al número de decimales especificados
    en el paréntesis, y regresar un valor flotante (dentro de la función round() se puede encontrar el 
    nombre de la variable, el nombre, una coma, y el número de decimales que se desean mostrar). 
    Fecha: 19 de septiembre'''
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

#2.4.1.10 LABORATORIO: Operadores y expresiones
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, 
    e imprime el valor de la variable llamada y.
    Fecha: 19 de septiembre'''
x =  -1
x = float(x)
y=(3*x**3)-(2*x**2)+3*x-1
print("y =", y)

#2.5.1.2 LABORATORIO: Comentarios
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: Calcula los segundos en cierto número de horas determinadas 
    Fecha: 19 de septiembre'''
a = 2 # número de horas
seconds = 3600 # número de segundos en una hora

print("Horas: ", a) 
print("Segundos en Horas: ", a * seconds) 

#2.6.1.9 LABORATORIO: Entradas y salidas simples
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: La tarea es completar el código para evaluar y mostrar el 
    resultado de cuatro operaciones aritméticas básicas.
    Fecha: 19 de septiembre'''
a=2.0 # ingresa un valor flotante para la variable a aquí
b=3.0 # ingresa un valor flotante para la variable b aquí

# muestra el resultado de la suma aquí 
print(a+b)
# muestra el resultado de la resta aquí
print(a-b)
# muestra el resultado de la multiplicación aquí
print(a*b)
# muestra el resultado de la división aquí
print(a/b)

print("\n¡Eso es todo, amigos!")

#2.6.1.10 LABORATORIO: Operadores y expresiones

x = float(input("Ingresa el valor para x: "))
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: El resultado debe de ser asignado a y. 
    Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis sean necesarios.
    Fecha: 19 de septiembre'''
# Escribe tu código aquí.
y=(1/(x+(1/(x+(1/(x+(1/x)))))))
print("y =", y)

#2.6.1.11 LABORATORIO: Operadores y expresiones
''' Nombre: Fabio Alonso Sánchez García
    Descripcion: La tarea es preparar un código simple para evaluar o encontrar el tiempo final
    de un periodo de tiempo dado, expresándolo en horas y minutos. 
    Fecha: 19 de septiembre'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
minutos_totales=mins+dura
minutos_sobrantes=minutos_totales%60

horas_totales=hour+minutos_totales//60

print(str(horas_totales)+":"+str(minutos_sobrantes))
