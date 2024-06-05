#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_MergeSort       5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def merge_sort(lista):
    # Caso base: si la longitud de la lista es menor o igual a 1, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Dividimos la lista en mitades izquierda y derecha
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Llamada recursiva para ordenar las mitades izquierda y derecha
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)
    
    # Combinamos las mitades ordenadas
    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
    # Inicializamos una lista vacía para almacenar la fusión de las mitades
    fusion = []
    
    # Índices para recorrer las listas izquierda y derecha
    i = j = 0
    
    # Recorremos ambas listas y fusionamos sus elementos en orden
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            fusion.append(izquierda[i])
            i += 1
        else:
            fusion.append(derecha[j])
            j += 1
    
    # Agregamos los elementos restantes de la lista izquierda (si los hay)
    while i < len(izquierda):
        fusion.append(izquierda[i])
        i += 1
    
    # Agregamos los elementos restantes de la lista derecha (si los hay)
    while j < len(derecha):
        fusion.append(derecha[j])
        j += 1
    
    return fusion

# Programa principal para demostrar el uso del algoritmo Merge Sort
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [12, 11, 13, 5, 6, 7]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo Merge Sort
    lista_ordenada = merge_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
