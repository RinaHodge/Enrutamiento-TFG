import heapq

from ClaseGrafo import Grafo

def Dijkstra(grafo, nodo_inicio):
    """
    Implementa el algoritmo de Dijkstra para encontrar las rutas más cortas desde un nodo de inicio.
    Argumentos:
        grafo (dict): Diccionario que representa el grafo con sus aristas y costes.
        nodo_inicio (str): Nodo desde el cual se calculan las rutas más cortas.
    Returns:
        dist (dict): Diccionario con las distancias mínimas desde el nodo de inicio a cada nodo.
        prev (dict): Diccionario con los predecesores de cada nodo en la ruta más corta.
    """
    
    dist = {}
    prev = {}

    # Inicializar distancias y predecesores
    for vertice in grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[nodo_inicio] = 0

    Q = [vertice for vertice in grafo]    # Conjunto de vértices no visitados

    while Q:
        u = min(Q, key=lambda vertice: dist[vertice])  # Vértice con la distancia mínima
        Q.remove(u)
        
        # Actualizar distancias a los vecinos
        for vecino in grafo[u]:
            # Si el vecino está en Q y se encuentra una ruta más corta
            if vecino in Q and dist[vecino] > dist[u] + grafo[u][vecino]:
                dist[vecino] = dist[u] + grafo[u][vecino]  
                prev[vecino] = u

    return dist, prev