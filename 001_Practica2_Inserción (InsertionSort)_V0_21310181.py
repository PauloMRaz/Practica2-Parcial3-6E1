#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_Inserción (InsertionSort)           5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def insertion_sort(lista):
    # Iteramos sobre cada elemento de la lista, comenzando desde el segundo elemento
    for i in range(1, lista.__len__()):
        # Almacenamos el valor actual en una variable temporal
        valor_actual = lista[i]
        # Inicializamos una variable para comparar con los elementos anteriores
        j = i - 1

        # Movemos los elementos de la lista que son mayores que valor_actual
        # una posición hacia adelante
        while j >= 0 and valor_actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        # Insertamos el valor_actual en su posición correcta
        lista[j + 1] = valor_actual

    return lista

# Programa principal para demostrar el uso del algoritmo de ordenación por inserción
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [12, 11, 13, 5, 6]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo de inserción
    lista_ordenada = insertion_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
