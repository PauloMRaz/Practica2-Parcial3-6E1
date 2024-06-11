#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 4_simulador Árbol Parcial mínimo de Prim.      5/06/2024
#¿Cómo se implementa en el mundo?
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Implementación del Algoritmo de Prim en una Aplicación de Redes de Telecomunicaciones
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class GrafoTelecomunicaciones:
    def __init__(self):
        # Inicializa un grafo con un diccionario vacío de vértices
        self.vertices = {}

    def agregar_vertice(self, vertice):
        # Agrega un vértice al grafo si no existe
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, origen, destino, distancia):
        # Agrega una arista entre dos vértices con una distancia dada
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.vertices[origen][destino] = distancia
        self.vertices[destino][origen] = distancia  # Para redes no dirigidas

    def prim(self, inicio):
        # Implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST)
        mst = []  # Lista para almacenar el Árbol de Expansión Mínima (MST)
        visitados = set([inicio])
        aristas = [(distancia, inicio, destino) for destino, distancia in self.vertices[inicio].items()]
        heapq.heapify(aristas)

        print(f"Iniciando desde el nodo {inicio}")

        while aristas:
            distancia, origen, destino = heapq.heappop(aristas)
            if destino not in visitados:
                visitados.add(destino)
                mst.append((origen, destino, distancia))
                print(f"Seleccionando arista ({origen} - {destino}) con distancia {distancia}")

                for siguiente_destino, siguiente_distancia in self.vertices[destino].items():
                    if siguiente_destino not in visitados:
                        heapq.heappush(aristas, (siguiente_distancia, destino, siguiente_destino))
        
        return mst

    def graficar(self, mst):
        # Crea y muestra un gráfico del Árbol de Expansión Mínima usando networkx y matplotlib
        G = nx.Graph()
        for origen, destino, distancia in mst:
            G.add_edge(origen, destino, weight=distancia)

        pos = nx.spring_layout(G)  # Posiciones de los nodos para el layout del grafo
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Árbol de Expansión Mínima (MST)")
        plt.show()

def main():
    # Crea una instancia del grafo de telecomunicaciones y agrega las aristas con sus respectivas distancias
    grafo_telecom = GrafoTelecomunicaciones()
    grafo_telecom.agregar_arista('Central', 'Nodo1', 10)
    grafo_telecom.agregar_arista('Central', 'Nodo2', 20)
    grafo_telecom.agregar_arista('Central', 'Nodo3', 15)
    grafo_telecom.agregar_arista('Nodo1', 'Nodo2', 25)
    grafo_telecom.agregar_arista('Nodo2', 'Nodo3', 30)

    # Define el nodo de inicio para el algoritmo de Prim
    inicio = 'Central'
    mst = grafo_telecom.prim(inicio)

    # Imprime el Árbol de Expansión Mínima
    print("\nÁrbol de Expansión Mínima:")
    for origen, destino, distancia in mst:
        print(f"Arista ({origen} - {destino}) con distancia {distancia}")

    # Genera y muestra el gráfico del Árbol de Expansión Mínima
    grafo_telecom.graficar(mst)

if __name__ == "__main__":
    main()

