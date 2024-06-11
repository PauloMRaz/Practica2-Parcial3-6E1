#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 5_simulador Árbol de Máximo y Mínimo coste Kruskal.      6/06/2024
#¿Cómo se implementa en el mundo?
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Redes de Distribución de Agua
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        # Inicializa el grafo con un conjunto de vértices y una lista de aristas
        self.vertices = set()
        self.aristas = []

    def agregar_arista(self, origen, destino, peso):
        # Agrega una arista al grafo, tanto en el conjunto de vértices como en la lista de aristas
        self.vertices.add(origen)
        self.vertices.add(destino)
        self.aristas.append((peso, origen, destino))

    def encontrar(self, padre, i):
        # Encuentra la raíz de un conjunto al que pertenece el elemento i
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])

    def union(self, padre, rango, x, y):
        # Realiza la unión de dos subconjuntos
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)

        # Une los árboles de forma que el árbol más pequeño quede bajo el más grande
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal(self, inverso=False):
        # Algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST)
        resultado = []  # Lista para almacenar el MST final
        i = 0  # Índice de las aristas ordenadas
        e = 0  # Contador de aristas en el MST

        # Ordena las aristas según su peso (ascendente para MST mínimo, descendente para MST máximo)
        self.aristas = sorted(self.aristas, key=lambda item: item[0], reverse=inverso)
        padre = {}
        rango = {}

        # Inicializa los conjuntos disjuntos
        for vertice in self.vertices:
            padre[vertice] = vertice
            rango[vertice] = 0

        # Itera hasta que el MST tenga |V| - 1 aristas
        while e < len(self.vertices) - 1:
            peso, origen, destino = self.aristas[i]
            i = i + 1
            x = self.encontrar(padre, origen)
            y = self.encontrar(padre, destino)

            # Si los vértices no forman un ciclo, añade la arista al resultado
            if x != y:
                e = e + 1
                resultado.append((origen, destino, peso))
                self.union(padre, rango, x, y)

        return resultado

def imprimir_resultado(mensaje, resultado):
    # Imprime el resultado del MST
    print(mensaje)
    for origen, destino, peso in resultado:
        print(f"Arista ({origen} - {destino}) con peso {peso}")

def dibujar_mst(resultado, mensaje):
    # Crea un objeto de gráfico de NetworkX
    G = nx.Graph()

    # Agrega las aristas del MST al gráfico
    for origen, destino, peso in resultado:
        G.add_edge(origen, destino, weight=peso)

    # Dibuja el gráfico
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrowsize=20)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(mensaje)
    
    # Muestra el gráfico en una ventana emergente separada
    plt.show()

def main():
    # Crea un nuevo grafo para representar la red de distribución de agua
    grafo = Grafo()
    # Agrega las aristas al grafo con los costos de instalación de las tuberías
    grafo.agregar_arista('Planta1', 'Distribuidor1', 10)
    grafo.agregar_arista('Planta1', 'Distribuidor2', 20)
    grafo.agregar_arista('Planta1', 'Distribuidor3', 30)
    grafo.agregar_arista('Distribuidor1', 'Distribuidor2', 5)
    grafo.agregar_arista('Distribuidor2', 'Distribuidor3', 15)
    grafo.agregar_arista('Distribuidor3', 'Planta2', 10)
    grafo.agregar_arista('Planta2', 'Distribuidor1', 25)
    grafo.agregar_arista('Planta2', 'Distribuidor2', 35)

    # Ejecuta el algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima
    print("Ejecutando Kruskal para encontrar el Árbol de Expansión Mínima:")
    mst_minimo = grafo.kruskal()
    imprimir_resultado("Árbol de Expansión Mínima:", mst_minimo)
    dibujar_mst(mst_minimo, "Árbol de Expansión Mínima")

    # Ejecuta el algoritmo de Kruskal para encontrar el Árbol de Expansión Máxima
    print("\nEjecutando Kruskal para encontrar el Árbol de Expansión Máxima:")
    mst_maximo = grafo.kruskal(inverso=True)
    imprimir_resultado("Árbol de Expansión Máxima:", mst_maximo)
    dibujar_mst(mst_maximo, "Árbol de Expansión Máxima")

if __name__ == "__main__":
    main()
