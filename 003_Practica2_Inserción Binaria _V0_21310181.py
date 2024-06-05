#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_Inserción Binaria           5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def insercion_binaria(lista):
    # Función auxiliar para encontrar el índice donde insertar el elemento usando búsqueda binaria
    def busqueda_binaria(sublista, valor):
        izquierda, derecha = 0, len(sublista) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if sublista[medio] < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return izquierda

    # Iteramos sobre cada elemento de la lista, comenzando desde el segundo elemento
    for i in range(1, len(lista)):
        # Almacenamos el valor actual en una variable temporal
        valor_actual = lista[i]
        # Realizamos la búsqueda binaria en la sublista ordenada
        posicion = busqueda_binaria(lista[:i], valor_actual)
        
        # Movemos los elementos para hacer espacio e insertamos el valor actual en la posición encontrada
        lista = lista[:posicion] + [valor_actual] + lista[posicion:i] + lista[i+1:]
    
    return lista

# Programa principal para demostrar el uso del algoritmo de inserción binaria
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo de inserción binaria
    lista_ordenada = insercion_binaria(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
