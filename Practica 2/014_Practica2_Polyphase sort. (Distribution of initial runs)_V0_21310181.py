#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_Polyphase sort. (Distribution of initial runs)    5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import heapq
import itertools
import random

def initial_runs_distribution(data, buffer_size):
    runs = []
    buffer = []
    current_run = []

    # Lee los datos de entrada y los divide en runs
    for item in data:
        current_run.append(item)
        if len(current_run) >= buffer_size:
            buffer.append(sorted(current_run))
            current_run = []

    # Si hay elementos restantes, se crea un último run
    if current_run:
        buffer.append(sorted(current_run))

    # Fusiona los runs de manera parcial y los almacena en disco
    while buffer:
        merged_run = list(heapq.merge(*buffer))
        runs.append(merged_run)
        buffer = [list(buffer_chunk) for buffer_chunk in chunks(merged_run, buffer_size)]

    return runs

def chunks(lst, n):
    """Divide la lista en trozos de tamaño n."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Programa principal para demostrar el uso de la distribución de runs iniciales en Polyphase Sort
def main():
    # Genera datos de entrada aleatorios
    data = [random.randint(1, 100) for _ in range(50)]
    print("Datos de entrada:", data)

    # Tamaño del buffer para la distribución de runs iniciales
    buffer_size = 10

    # Ejecuta la fase de distribución inicial
    initial_runs = initial_runs_distribution(data, buffer_size)

    # Imprime los runs resultantes
    print("Runs iniciales:")
    for i, run in enumerate(initial_runs):
        print(f"Run {i + 1}: {run}")

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
