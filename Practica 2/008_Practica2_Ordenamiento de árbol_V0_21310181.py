#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 2_Ordenamiento de árbol       5/06/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

class Nodo:
    def __init__(self, valor):
        # Inicializamos el nodo con su valor y sus hijos izquierdo y derecho
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        # Inicializamos el árbol con la raíz como None
        self.raiz = None

    def insertar(self, valor):
        # Si la raíz es None, el nuevo nodo será la raíz
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            # Llamamos a la función auxiliar para insertar recursivamente
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        # Si el valor es menor que el nodo actual, vamos al subárbol izquierdo
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            # Si el valor es mayor o igual, vamos al subárbol derecho
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def en_orden(self):
        # Lista para almacenar los elementos en orden
        elementos = []
        # Llamamos a la función auxiliar para recorrer el árbol en orden
        self._en_orden_recursivo(self.raiz, elementos)
        return elementos

    def _en_orden_recursivo(self, nodo, elementos):
        if nodo:
            # Recursivamente recorremos el subárbol izquierdo
            self._en_orden_recursivo(nodo.izquierdo, elementos)
            # Agregamos el valor del nodo actual
            elementos.append(nodo.valor)
            # Recursivamente recorremos el subárbol derecho
            self._en_orden_recursivo(nodo.derecho, elementos)

def tree_sort(lista):
    # Creamos una instancia del Árbol Binario de Búsqueda
    abb = ArbolBinarioBusqueda()
    # Insertamos cada elemento de la lista en el árbol
    for valor in lista:
        abb.insertar(valor)
    # Obtenemos los elementos en orden
    return abb.en_orden()

# Programa principal para demostrar el uso del algoritmo Tree Sort
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [64, 25, 12, 22, 11]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo Tree Sort
    lista_ordenada = tree_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
