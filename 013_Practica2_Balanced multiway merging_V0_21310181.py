#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_Balanced multiway merging    5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import heapq

def balanced_multiway_merging(arrays):
    result = []
    heap = [(arr[0], i, 0) for i, arr in enumerate(arrays) if arr]

    heapq.heapify(heap)

    while heap:
        val, array_idx, idx = heapq.heappop(heap)
        result.append(val)

        if idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][idx + 1]
            heapq.heappush(heap, (next_val, array_idx, idx + 1))

    return result

# Programa principal para demostrar el uso del algoritmo Balanced Multiway Merging
def main():
    # Ejemplo de listas desordenadas
    arrays = [
        [3, 5, 7],
        [1, 4, 6],
        [2, 8, 9]
    ]
    print("Listas desordenadas:", arrays)

    # Ordenamos las listas utilizando el algoritmo Balanced Multiway Merging
    lista_ordenada = balanced_multiway_merging(arrays)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
