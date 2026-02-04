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

def reconstruir_ruta(prev, nodo_inicio, nodo_fin):
    """
    Reconstruye la ruta más corta desde el nodo de inicio al nodo de fin utilizando el diccionario de predecesores.

    Argumentos:
        prev (dict): Diccionario con los predecesores de cada nodo en la ruta más corta.
        nodo_inicio (str): Nodo de inicio.
        nodo_fin (str): Nodo de fin.

    Returns:
        ruta (list): Lista que representa la ruta más corta desde el nodo de inicio al nodo de fin.
    """
    ruta = []
    actual = nodo_fin

    while actual is not None:
        ruta.append(actual)
        actual = prev[actual]

    ruta.reverse()  # Invertir la ruta para obtener el orden correcto desde inicio a fin

    if ruta[0] == nodo_inicio:
        return ruta
    else:
        return []  # No hay ruta desde nodo_inicio a nodo_fin
    
def calcular_coste_ruta(grafo, ruta):
    """
    Calcula el coste total de una ruta dada en el grafo.

    Argumentos:
        grafo (dict): Diccionario que representa el grafo con sus aristas y costes.
        ruta (list): Lista que representa la ruta para la cual se desea calcular el coste.

    Returns:
        float: Coste total de la ruta. Si la ruta no es válida, devuelve float('inf').
    """
    coste_total = 0

    for i in range(len(ruta) - 1):
        origen = ruta[i]
        destino = ruta[i + 1]

        if destino in grafo[origen]:
            coste_total += grafo[origen][destino]
        else:
            return float('inf')  # Ruta no válida si no hay enlace entre origen y destino

    return coste_total

def yen_k_shortest_paths(graph, source, target, k):
        """
        Encuentra las k rutas más cortas entre el nodo source y el nodo target en el grafo dado utilizando el algoritmo de Yen.
        Argumentos:
            graph (networkx.Graph): El grafo donde se buscarán las rutas.
            source (node): Nodo de origen.
            target (node): Nodo de destino.
            k (int): Número de rutas más cortas a encontrar.
        Returns:
            list: Una lista de listas, donde cada sublista representa una ruta desde source hasta target.
        """

        if source == target:
            return [[source]]

        paths = []
        potential_paths = []

        dist, prev = Dijkstra(graph.grafo, source)
        
        # Primer camino más corto usando Dijkstra
        try:
            first_path = reconstruir_ruta(prev, source, target)

            if not first_path:
                return []       # No hay ruta entre source y target
            
            paths.append(first_path)
        except:
            return []

        # Encontrar las k-1 rutas más cortas adicionales
        for i in range(1, k):
            for j in range(len(paths[-1]) - 1):
                spur_node = paths[-1][j]
                root_path = paths[-1][:j + 1]

                g_copy = graph.copiar_grafo()

                # Remover las aristas que ya están en las rutas encontradas
                for path in paths:
                    if path[:j + 1] == root_path and len(path) > j + 1:
                        g_copy.eliminar_arista(path[j], path[j + 1])

                # Remover los nodos del camino raíz excepto el nodo de la raíz
                for node in root_path[:-1]:
                    g_copy.eliminar_nodo(node)
                try:
                    dist_spur, prev_spur = Dijkstra(g_copy.grafo, spur_node)
                    spur_path = reconstruir_ruta(prev_spur, spur_node, target)
                    
                    # Verificar si se encontró un camino spur
                    if spur_path:
                        total_path = root_path[:-1] + spur_path
                        total_weight = sum(
                            graph.grafo[u][v] for u, v in zip(total_path, total_path[1:])
                        )
                    
                    # Evistar rutas duplicadas
                    if (total_weight, total_path) not in potential_paths:
                        heapq.heappush(potential_paths, (total_weight, total_path))
                except Exception:
                    continue

            if potential_paths:
                _, new_path = heapq.heappop(potential_paths)
                paths.append(new_path)
            else:
                break

        return paths