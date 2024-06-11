#Paulo Enrique Muñoz Razón      21310181     
#3er Parcial 
#Practica 5_simulador Árbol de Máximo y Mínimo coste Kruskal.      6/06/2024
#¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño?
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Planificación de Redes de Suministro de Agua
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.vertices = set()  # Conjunto de todos los vértices del grafo
        self.aristas = []  # Lista de todas las aristas del grafo

    def agregar_arista(self, origen, destino, peso):
        """Agrega una arista al grafo"""
        self.vertices.add(origen)  # Añade el vértice de origen al conjunto de vértices
        self.vertices.add(destino)  # Añade el vértice de destino al conjunto de vértices
        self.aristas.append((peso, origen, destino))  # Añade la arista (con su peso) a la lista de aristas

    def encontrar(self, padre, i):
        """Función auxiliar para encontrar el conjunto al que pertenece un elemento"""
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])  # Encuentra el conjunto de manera recursiva

    def union(self, padre, rango, x, y):
        """Función auxiliar para unir dos conjuntos"""
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)

        # Une los conjuntos basándose en el rango
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal(self):
        """Implementación del algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima"""
        resultado = []  # Lista para almacenar el Árbol de Expansión Mínima
        i = 0  # Índice para las aristas ordenadas
        e = 0  # Contador de aristas incluidas en el resultado

        # Ordena todas las aristas del grafo según su peso
        self.aristas = sorted(self.aristas, key=lambda item: item[0])

        padre = {}  # Diccionario para almacenar los padres de los vértices
        rango = {}  # Diccionario para almacenar los rangos de los vértices

        # Inicializa los conjuntos de los vértices
        for vertice in self.vertices:
            padre[vertice] = vertice
            rango[vertice] = 0

        # Recorre todas las aristas ordenadas
        while e < len(self.vertices) - 1:
            peso, origen, destino = self.aristas[i]
            i = i + 1
            x = self.encontrar(padre, origen)
            y = self.encontrar(padre, destino)

            # Incluye la arista en el resultado si no forma un ciclo
            if x != y:
                e = e + 1
                resultado.append((origen, destino, peso))
                self.union(padre, rango, x, y)

        return resultado  # Devuelve el Árbol de Expansión Mínima

def imprimir_resultado(mensaje, resultado):
    """Imprime el resultado del Árbol de Expansión Mínima"""
    print(mensaje)
    for origen, destino, peso in resultado:
        print(f"Tubería de {origen} a {destino} con diámetro {peso} pulgadas")

def graficar_arbol(grafo, resultado):
    """Grafica el Árbol de Expansión Mínima"""
    G = nx.Graph()

    # Agregar aristas con sus pesos al grafo de NetworkX
    for origen, destino, peso in resultado:
        G.add_edge(origen, destino, weight=peso)

    # Obtener posición de los nodos para un mejor trazado
    pos = nx.spring_layout(G)

    # Dibujar nodos y aristas
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    # Agregar etiquetas de peso a las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Mostrar la gráfica
    plt.title("Árbol de Mínimo Coste")
    plt.axis('off')
    plt.show()

def main():
    # Crear una instancia del grafo
    grafo = Grafo()

    # Agregar aristas al grafo representando las tuberías entre distintas ubicaciones
    grafo.agregar_arista('Planta de Tratamiento', 'Zona Residencial', 8)
    grafo.agregar_arista('Planta de Tratamiento', 'Industria', 10)
    grafo.agregar_arista('Planta de Tratamiento', 'Zona Comercial', 6)
    grafo.agregar_arista('Zona Residencial', 'Parque', 5)
    grafo.agregar_arista('Zona Comercial', 'Parque', 7)
    grafo.agregar_arista('Industria', 'Parque', 9)

    # Ejecutar el algoritmo de Kruskal para encontrar el MST
    print("Ejecutando Kruskal para planificar la red de suministro de agua:")
    mst_minimo = grafo.kruskal()

    # Imprimir el resultado del MST
    imprimir_resultado("Planificación de tuberías:", mst_minimo)

    # Graficar el Árbol de Expansión Mínima
    graficar_arbol(grafo, mst_minimo)

if __name__ == "__main__":
    main()

