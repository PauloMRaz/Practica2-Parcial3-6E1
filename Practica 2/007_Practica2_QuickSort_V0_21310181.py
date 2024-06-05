#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_QuickSort         5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def quick_sort(lista):
    # Función auxiliar para realizar la partición
    def particion(lista, bajo, alto):
        # Elegimos el último elemento como pivote
        pivote = lista[alto]
        # Inicializamos el índice del elemento más pequeño
        i = bajo - 1

        # Recorremos la lista desde bajo hasta alto-1
        for j in range(bajo, alto):
            # Si el elemento actual es menor o igual al pivote
            if lista[j] <= pivote:
                # Incrementamos el índice del elemento más pequeño
                i += 1
                # Intercambiamos el elemento actual con el elemento en el índice i
                lista[i], lista[j] = lista[j], lista[i]

        # Intercambiamos el pivote con el elemento en el índice i+1
        lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
        # Devolvemos el índice del pivote
        return i + 1

    # Función recursiva para realizar QuickSort
    def quick_sort_recursivo(lista, bajo, alto):
        if bajo < alto:
            # Obtenemos el índice del pivote
            pi = particion(lista, bajo, alto)
            # Aplicamos QuickSort a la sublista izquierda
            quick_sort_recursivo(lista, bajo, pi - 1)
            # Aplicamos QuickSort a la sublista derecha
            quick_sort_recursivo(lista, pi + 1, alto)

    # Llamamos a la función recursiva con los parámetros iniciales
    quick_sort_recursivo(lista, 0, len(lista) - 1)
    return lista

# Programa principal para demostrar el uso del algoritmo de QuickSort
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [10, 7, 8, 9, 1, 5]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo QuickSort
    lista_ordenada = quick_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
