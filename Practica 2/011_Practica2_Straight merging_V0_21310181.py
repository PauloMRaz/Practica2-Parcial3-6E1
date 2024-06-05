#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_Straight merging      5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def straight_insertion_sort(arr, izquierda, derecha):
    # Ordena el subarreglo utilizando el método de ordenación Straight Insertion
    for i in range(izquierda + 1, derecha + 1):
        clave = arr[i]
        j = i - 1
        while j >= izquierda and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

def straight_merging(arr):
    n = len(arr)
    tamano_actual = 1

    # Fusiona subarreglos de tamaño 1, 2, 4, 8, ... hasta que el tamaño del subarreglo sea igual al tamaño del array
    while tamano_actual <= n - 1:
        # Escoge el índice de inicio de cada subarreglo y el índice de inicio del segundo subarreglo
        izquierda = 0
        while izquierda < n - 1:
            # Calcula el índice de inicio del segundo subarreglo
            medio = min(izquierda + tamano_actual - 1, n - 1)
            derecha = min(izquierda + 2 * tamano_actual - 1, n - 1)

            # Fusiona los dos subarreglos
            straight_insertion_sort(arr, izquierda, medio)
            straight_insertion_sort(arr, medio + 1, derecha)

            # Une los dos subarreglos fusionados
            merge(arr, izquierda, medio, derecha)

            # Mueve el índice de inicio al inicio del siguiente par de subarreglos
            izquierda = izquierda + 2 * tamano_actual

        # Aumenta el tamaño del subarreglo
        tamano_actual = 2 * tamano_actual

def merge(arr, izquierda, medio, derecha):
    n1 = medio - izquierda + 1
    n2 = derecha - medio

    # Crea arreglos temporales para almacenar los subarreglos izquierdo y derecho
    izq = [0] * n1
    der = [0] * n2

    # Copia los datos a los arreglos temporales
    for i in range(n1):
        izq[i] = arr[izquierda + i]
    for j in range(n2):
        der[j] = arr[medio + 1 + j]

    # Fusiona los arreglos temporales de vuelta al arreglo original
    i = j = 0
    k = izquierda

    while i < n1 and j < n2:
        if izq[i] <= der[j]:
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1
        k += 1

    # Copia los elementos restantes de izq[] si los hay
    while i < n1:
        arr[k] = izq[i]
        i += 1
        k += 1

    # Copia los elementos restantes de der[] si los hay
    while j < n2:
        arr[k] = der[j]
        j += 1
        k += 1

# Programa principal para demostrar el uso del algoritmo Straight Merging
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [12, 11, 13, 5, 6, 7]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo Straight Merging
    straight_merging(lista_desordenada)
    print("Lista ordenada:", lista_desordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
