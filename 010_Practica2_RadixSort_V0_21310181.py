#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_RadixSort       5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def counting_sort(arr, exp):
    n = len(arr)

    # Inicializamos el array de conteo con 10 posiciones (0-9)
    count = [0] * 10
    output = [0] * n

    # Contamos la frecuencia de cada dígito en la posición exp
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calculamos las posiciones finales de cada dígito en el array ordenado
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construimos el array ordenado
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copiamos el array ordenado al array original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Obtenemos el máximo número del array para saber el número de dígitos
    max_num = max(arr)

    # Aplicamos counting sort para cada dígito, empezando por el menos significativo
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Programa principal para demostrar el uso del algoritmo Radix Sort
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo Radix Sort
    radix_sort(lista_desordenada)
    print("Lista ordenada:", lista_desordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
