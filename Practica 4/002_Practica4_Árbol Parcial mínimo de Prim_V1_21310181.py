#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 4_simulador Árbol Parcial mínimo de Prim.      5/06/2024
#¿Cómo lo implementarías en tu vida?
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Optimización de Rutas de Viaje
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        # Inicializa un diccionario vacío para almacenar los vértices
        self.vertices = {}

    def agregar_vertice(self, vertice):
        # Agrega un vértice al grafo si no existe
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        # Agrega una arista con un peso entre dos vértices
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.vertices[origen].append((peso, destino))
        self.vertices[destino].append((peso, origen))  # Para grafos no dirigidos

    def prim(self, inicio):
        # Implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST)
        mst = []  # Lista para almacenar el MST
        visitados = set([inicio])
        aristas = [(peso, inicio, destino) for peso, destino in self.vertices[inicio]]
        heapq.heapify(aristas)

        print(f"Comenzando en el nodo {inicio}")

        while aristas:
            peso, origen, destino = heapq.heappop(aristas)
            if destino not in visitados:
                visitados.add(destino)
                mst.append((origen, destino, peso))
                print(f"Seleccionando arista ({origen} - {destino}) {peso} minutos")

                for siguiente_peso, siguiente_destino in self.vertices[destino]:
                    if siguiente_destino not in visitados:
                        heapq.heappush(aristas, (siguiente_peso, destino, siguiente_destino))
        
        return mst

    def graficar(self, mst):
        # Crea y muestra un gráfico del Árbol de Expansión Mínima usando networkx y matplotlib
        G = nx.Graph()
        for origen, destino, peso in mst:
            G.add_edge(origen, destino, weight=peso)

        pos = nx.spring_layout(G)  # Posiciones de los nodos para el layout del grafo
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Árbol de Expansión Mínima (MST)")
        plt.show()

def main():
    # Crea una instancia del grafo y agrega las aristas con sus respectivos pesos
    grafo = Grafo()
    grafo.agregar_arista('Centro', 'Zapopan', 10)
    grafo.agregar_arista('Centro', 'Tlaquepaque', 12)
    grafo.agregar_arista('Centro', 'Tonalá', 15)
    grafo.agregar_arista('Centro', 'Tlajomulco', 25)
    grafo.agregar_arista('Zapopan', 'Tlaquepaque', 18)
    grafo.agregar_arista('Zapopan', 'Tonalá', 20)
    grafo.agregar_arista('Tlaquepaque', 'Tlajomulco', 22)
    grafo.agregar_arista('Tonalá', 'Tlajomulco', 30)

    # Define el nodo de inicio para el algoritmo de Prim
    inicio = 'Centro'
    mst = grafo.prim(inicio)

    # Imprime el Árbol de Expansión Mínima
    print("\nÁrbol de Expansión Mínima:")
    for origen, destino, peso in mst:
        print(f"Arista ({origen} - {destino}) {peso} minutos")

    # Genera y muestra el gráfico del Árbol de Expansión Mínima
    grafo.graficar(mst)

if __name__ == "__main__":
    main()

