# Practica 1 - Medicion empirica de complejidad
#Axel Guillermo Martinez Martinez
# Analisis de Algoritmos
# Codigo base de ejemplo
# Lenguaje: Python 3

import time
import random

def recorrido_simple(lista):                                    #declaramos funcion para el recorrido simple
    total = 0
    for x in lista:  
        total += x                                               #recorre la lista y se va haciendo la sumatoria de los elementos en ella
    return total                                                 #retorna el total final al terminar el recorrido

def doble_ciclo(lista):                                         #declaramos funcion para el  doble ciclo
    contador = 0    
    for i in range(len(lista)):                                 #recorrido que se hace en el rango de los elementos de la lista
        for j in range(len(lista)):                             #recorrido anidado tambien en el rango de los elementos de la lista
            contador += lista[i] * lista[j]                     #contador va a multiplicar el lo que hay en la posicion i con la de j 
    return contador                                             #retorna el valor final de contador

def experimento():                                              #Funcion donde se llevaran a cabo las pruebas

    tamanios = [100, 500, 1000, 2000]                           #array con los tamaños de elementos
    print("Tamano | Recorrido simple (s) | Doble ciclo (s)")
    print("----------------------------------------------")

    for n in tamanios:                                          #bucle for que a cada elemento de el array tamanios
        datos = [random.randint(1, 100) for _ in range(n)]      #llena un array de numeros random del 1 al 100 con un bucle para llenarlo todo

        inicio = time.time()                                    #guarda el tiempo en una variable para el inicio
        recorrido_simple(datos)                                 #llamamos la funcion del recorrido simple con como parametro datos que primero seran 100, luego 500, etc
        t1 = time.time() - inicio                               #guardamos el tiempo que le tomó y le restamos el tiempo inicial 

        inicio = time.time()                                    #guarda el tiempo en una variable para el inicio
        doble_ciclo(datos)                                      #llamamos la funcion del doble ciclo con como parametro datos
        t2 = time.time() - inicio                               #t2 guarda el tiempo que le tomo realizar la operacion y le resta el tiempo de inicio

        '''
        imprime en tabla primero n que tomara 6 espacios para alinear la tabla, dependiendo la iteración sera el elemento que este en 'tamanios' que es el tamaño de elementos,
        luego se imprime el tiempo de recorrido simple con 20 espacios y 6 decimales y el del doble ciclo tambien con 20 espacios y 6 decimales
        '''
        print(f"{n:6d} | {t1:20.6f} | {t2:15.6f}")        

if __name__ == "__main__":
    experimento()
