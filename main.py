# Mensaje dinámico
import os
import time 
#Importamos todas las funciones explicitas de nuestro módulo
import f_suma
#from f_suma import func_suma

while True:
    os.system ("clear")
    try:
        a = int(input("Ingresa el primer numero: \n")) #Solicitamos el 1er numero al usuario
        b = int(input("Ingresa el segundo numero: \n"))#Solicitamos el 2do numero al usuario
        opcion = int(input('Por favor seleccione una numero segun la opción: '))
        print("╔════════════════════════════════════╗")
        print('║ Nombre : Carlos Alember            ║')
        print('║ Aula   : 01                        ║')
        print('║      ISPC May 2022                 ║')
        print("╠════════════════════════════════════╣")
        print('║ 1.- Suma +                         ║')
        print('║ 2.- Resta –                        ║')
        print('║ 3.- Multiplicación *               ║')
        print('║ 4.- División /                     ║')
        print('║ 5.- División entera //             ║')
        print('║ 6.- Módulo (resto) %               ║')
        print('║ 7.- Potenciación **                ║')    
        print('║ 8.- Salir                          ║')
        print("╚════════════════════════════════════╝")
        if opcion == 1:
            print("El resultado es {}", func_suma(a, b)) 
        elif opcion == 2:
            print("Función resta dos numero enteros", opcion)
        elif opcion == 3:
            print("Función multiplica dos numero enteros", opcion)
        elif opcion == 4:
            print("Función división normal entre dos numero enteros", opcion)
        elif opcion == 5:
            print("Función división entera entre dos numero enteros", opcion)
        elif opcion == 6:
            print("Función modulo entera entre dos numero enteros",opcion)   
        elif opcion == 7:
            print("Función potencia entera entre dos numero enteros",opcion)                                    
        elif opcion == 8:
            print('Hasta la vista Baby q(❂‿❂)p ')
            break
        else:
            raise ValueError
    except ValueError:
        print('Ingrese solo números.(1 o 2 o 3 o 4 o 5 o 6 o 7 o 8)')