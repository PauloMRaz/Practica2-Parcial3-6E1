#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_Natural merging     5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def natural_merging_sort(arr):
    n = len(arr)
    
    # Realizamos el primer paso: dividir la lista en subsecuencias ordenadas
    sublistas = divide_sublistas(arr, n)
    
    # Fusionamos las sublistas ordenadas hasta que solo quede una sublista
    while len(sublistas) > 1:
        sublistas = merge_sublistas(sublistas)
    
    # La lista final es la única sublista restante
    return sublistas[0]

def divide_sublistas(arr, n):
    sublistas = []
    i = 0
    
    while i < n:
        sublista = [arr[i]]
        i += 1
        
        # Agregamos elementos a la sublista mientras estén en orden
        while i < n and arr[i] >= arr[i - 1]:
            sublista.append(arr[i])
            i += 1
        
        sublistas.append(sublista)
    
    return sublistas

def merge_sublistas(sublistas):
    result = []
    i = 0
    
    # Fusionamos pares de sublistas ordenadas
    while i < len(sublistas) - 1:
        merged = merge(sublistas[i], sublistas[i + 1])
        result.append(merged)
        i += 2
    
    # Si hay una sublista impar al final, la agregamos sin fusionar
    if i == len(sublistas) - 1:
        result.append(sublistas[i])
    
    return result

def merge(sublista1, sublista2):
    merged = []
    i = j = 0
    
    # Fusionamos las dos sublistas ordenadas
    while i < len(sublista1) and j < len(sublista2):
        if sublista1[i] <= sublista2[j]:
            merged.append(sublista1[i])
            i += 1
        else:
            merged.append(sublista2[j])
            j += 1
    
    # Agregamos los elementos restantes de ambas sublistas
    merged.extend(sublista1[i:])
    merged.extend(sublista2[j:])
    
    return merged

# Programa principal para demostrar el uso del algoritmo de fusión natural
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [12, 11, 13, 5, 6, 7]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo de fusión natural
    lista_ordenada = natural_merging_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
