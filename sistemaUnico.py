print("*** Bienvenido al Sistema de generación de identificación (ID) y correo único ***\n Por favor, ingresa tus datos: ")
from random import randint

#Recepción de datos:
nombre = input("Nombre: ")
apellido = input("Apellido: ")
nacimiento = input("Año en el que naciste (YYYY): ")

#Generador de ID:
nombre_1 = nombre[0:2].upper()
apellido_1 = apellido[0:2].upper()
nacimiento_1 = nacimiento[2:4]

aleatorio = randint(0,9999)
id = f'''{nombre_1}{apellido_1}{nacimiento_1}{aleatorio}'''

#Generador correo electrónico:
nombre_2 = nombre.lower()
apellido_2 = apellido.lower()

email = f'''{nombre_2}.{apellido_2}@correo.com'''

#Impresión en consola:
print(f'''Hola {nombre}!\n\tTu número de identificación único (ID) generado por el sistema es:\n\t{id}\n\tTu nuevo correo electrónico es:\n\t{email}\n\t***Hasta luego!*** ''')
