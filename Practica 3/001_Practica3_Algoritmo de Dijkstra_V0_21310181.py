#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 3_Algoritmo de Dijkstra      5/06/2024
#¿Cómo se implementa en el mundo?
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        # Inicializa un grafo con un diccionario vacío de vértices
        self.vertices = {}

    def agregar_vertice(self, vertice):
        # Agrega un vértice al grafo
        self.vertices[vertice] = {}

    def agregar_arista(self, origen, destino, peso):
        # Agrega una arista entre dos vértices con un peso dado
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen][destino] = peso

    def dijkstra(self, origen):
        # Implementa el algoritmo de Dijkstra para encontrar las distancias más cortas desde un origen dado
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[origen] = 0
        cola_prioridad = [(0, origen)]

        while cola_prioridad:
            # Extrae el vértice con la distancia mínima de la cola de prioridad
            distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

            # Si la distancia actual es mayor que la registrada, continúa con el siguiente ciclo
            if distancia_actual > distancias[vertice_actual]:
                continue

            # Revisa los vecinos del vértice actual
            for vecino, peso in self.vertices[vertice_actual].items():
                distancia = distancia_actual + peso
                # Si se encuentra una distancia más corta, actualiza la distancia y agrega el vecino a la cola de prioridad
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return distancias

    def graficar(self):
        # Crea y muestra un gráfico del grafo usando networkx y matplotlib
        G = nx.DiGraph()
        for vertice in self.vertices:
            G.add_node(vertice)
        for origen in self.vertices:
            for destino, peso in self.vertices[origen].items():
                G.add_edge(origen, destino, weight=peso)

        pos = nx.spring_layout(G)  # Posiciones de los nodos para el layout del grafo
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrowsize=20)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

def solicitar_datos_grafo():
    # Solicita al usuario los datos para construir el grafo
    grafo = Grafo()
    cantidad_vertices = int(input("Ingrese el número de nodos en el grafo: "))

    for _ in range(cantidad_vertices):
        vertice = input("Ingrese el nombre del nodo: ")
        grafo.agregar_vertice(vertice)

    cantidad_aristas = int(input("Ingrese el número de aristas en el grafo: "))

    for _ in range(cantidad_aristas):
        origen, destino, peso = input("Ingrese la arista (origen destino peso): ").split()
        peso = int(peso)
        grafo.agregar_arista(origen, destino, peso)

    return grafo

def main():
    print("Bienvenido al simulador de Algoritmo de Dijkstra.")
    print("Por favor, ingrese los detalles del grafo.")

    # Solicita los detalles del grafo al usuario
    grafo = solicitar_datos_grafo()

    # Solicita el nodo de inicio para ejecutar el algoritmo de Dijkstra
    origen = input("Ingrese el nodo de inicio para el algoritmo de Dijkstra: ")

    # Calcula las distancias más cortas desde el nodo de inicio
    distancias = grafo.dijkstra(origen)

    # Imprime las distancias más cortas desde el nodo de inicio a todos los demás nodos
    print("\nDistancias más cortas desde el nodo de inicio (" + origen + "):")
    for vertice, distancia in distancias.items():
        print(f"Distancia a {vertice}: {distancia}")

    # Genera y muestra el gráfico del grafo
    grafo.graficar()

if __name__ == "__main__":
    main()


