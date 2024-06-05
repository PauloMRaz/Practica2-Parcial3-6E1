#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_ShellSort          5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def shell_sort(lista):
    # Calculamos el tamaño de la lista
    n = len(lista)
    # Inicializamos el valor de gap (distancia entre los elementos a comparar)
    gap = n // 2

    # Mientras gap sea mayor que 0
    while gap > 0:
        # Iteramos sobre los elementos de la lista desde gap hasta el final
        for i in range(gap, n):
            # Almacenamos el valor actual en una variable temporal
            temp = lista[i]
            # Inicializamos una variable j para comparar y mover los elementos
            j = i

            # Desplazamos los elementos de la lista que están gap posiciones atrás
            # y son mayores que temp hacia adelante
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap

            # Insertamos el valor temporal en su posición correcta
            lista[j] = temp

        # Reducimos el gap para la siguiente iteración
        gap //= 2

    return lista

# Programa principal para demostrar el uso del algoritmo de Shell Sort
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [12, 34, 54, 2, 3]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo de Shell Sort
    lista_ordenada = shell_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
