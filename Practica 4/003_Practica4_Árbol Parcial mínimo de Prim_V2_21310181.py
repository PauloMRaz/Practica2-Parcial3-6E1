#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 4_simulador Árbol Parcial mínimo de Prim.      5/06/2024
#¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño?
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Despliegue de Redes de IoT (Internet de las cosas)
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class GrafoIoT:
    def __init__(self):
        # Inicializa un diccionario vacío para almacenar los vértices
        self.vertices = {}

    def agregar_dispositivo(self, dispositivo):
        # Agrega un dispositivo al grafo
        if dispositivo not in self.vertices:
            self.vertices[dispositivo] = {}

    def agregar_enlace(self, dispositivo1, dispositivo2, distancia):
        # Agrega un enlace entre dos dispositivos con una distancia especificada
        self.agregar_dispositivo(dispositivo1)
        self.agregar_dispositivo(dispositivo2)
        self.vertices[dispositivo1][dispositivo2] = distancia
        self.vertices[dispositivo2][dispositivo1] = distancia  # Para redes no dirigidas

    def prim(self, inicio):
        # Implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST)
        mst = []  # Lista para almacenar el MST
        visitados = set([inicio])
        aristas = [(distancia, inicio, dispositivo) for dispositivo, distancia in self.vertices[inicio].items()]
        heapq.heapify(aristas)

        print(f"Iniciando desde el dispositivo {inicio}")

        while aristas:
            distancia, origen, dispositivo = heapq.heappop(aristas)
            if dispositivo not in visitados:
                visitados.add(dispositivo)
                mst.append((origen, dispositivo, distancia))
                print(f"Seleccionando enlace ({origen} - {dispositivo}) con distancia {distancia}")

                for siguiente_dispositivo, siguiente_distancia in self.vertices[dispositivo].items():
                    if siguiente_dispositivo not in visitados:
                        heapq.heappush(aristas, (siguiente_distancia, dispositivo, siguiente_dispositivo))
        
        return mst

    def graficar(self, mst):
        # Crea y muestra un gráfico del Árbol de Expansión Mínima usando networkx y matplotlib
        G = nx.Graph()
        for origen, destino, distancia in mst:
            G.add_edge(origen, destino, weight=distancia)

        pos = nx.spring_layout(G)  # Posiciones de los nodos para el layout del grafo
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Árbol de Expansión Mínima (MST) para Dispositivos IoT")
        plt.show()

def main():
    # Crea una instancia del grafo y agrega los enlaces entre los dispositivos
    grafo_iot = GrafoIoT()
    grafo_iot.agregar_enlace('Sensor1', 'Gateway', 10)
    grafo_iot.agregar_enlace('Sensor2', 'Gateway', 15)
    grafo_iot.agregar_enlace('Sensor3', 'Gateway', 20)

    # Define el dispositivo de inicio para el algoritmo de Prim
    inicio = 'Gateway'
    mst = grafo_iot.prim(inicio)

    # Imprime el Árbol de Expansión Mínima
    print("\nÁrbol de Expansión Mínima:")
    for origen, dispositivo, distancia in mst:
        print(f"Enlace ({origen} - {dispositivo}) con distancia {distancia}")

    # Genera y muestra el gráfico del Árbol de Expansión Mínima
    grafo_iot.graficar(mst)

if __name__ == "__main__":
    main()
