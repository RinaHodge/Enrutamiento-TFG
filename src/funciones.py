import heapq

from src.clase_grafo import Grafo

def mapeo_letra(indice):
    """
    Mapea un índice numérico a una letra correspondiente (0 -> A, 1 -> B, etc.).

    Argumentos:
        indice (int): Índice numérico a mapear.

    Returns:
        str: Letra correspondiente al índice.
    """
    return chr(ord('A') + indice)


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
            coste_enlace = grafo[u][vecino]['coste']  # Obtener el coste de la arista entre u y su vecino
            # Si el vecino está en Q y se encuentra una ruta más corta
            if vecino in Q and dist[vecino] > dist[u] + coste_enlace:
                dist[vecino] = dist[u] + coste_enlace
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
            coste_total += grafo[origen][destino]['coste']  # Sumar el coste de la arista entre origen y destino
        else:
            return float('inf')  # Ruta no válida si no hay enlace entre origen y destino

    return coste_total

def yen_k_shortest_paths(graph, source, target, k):
        """
        Encuentra las k rutas más cortas entre el nodo source y el nodo target en el grafo dado utilizando el algoritmo de Yen.
        Argumentos:
            graph (Grafo): El grafo donde se buscarán las rutas.
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
                            graph.grafo[u][v]['coste'] for u, v in zip(total_path, total_path[1:])
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

def enrutar(grafo, trafico, k):
    """
    Función principal para enrutar el tráfico utilizando el algoritmo de Yen para encontrar las k rutas más cortas.

    Argumentos:
        grafo (Grafo): Instancia del grafo que representa la topología de la red.
        trafico (Trafico): Instancia del tráfico que contiene la matriz de tráfico y la matriz restante.
        k (int): Número de rutas más cortas a encontrar para cada par de nodos.

    Returns:
        dict: Un diccionario con las rutas guardadas para cada par de nodos.
        exito (bool): Indica si se han podido enrutar todas las demandas o no.
    """

    # grafo temporal 
    g_temp = grafo.copiar_grafo()   
    exito = True
    rutas_guardadas = {}     # Guardará las rutas definitivas por las que se enrutarán. 
    trafico.ordenar_capacidad()  # Ordenar la lista de demandas por demanda de mayor a menor
    # Recorrer la lista de demandas
    while True:
        demanda_info = trafico.mayor_demanda()  # Obtener la demanda más alta de la lista
        if demanda_info is None: 
            break  
        demanda, (origen, destino) = demanda_info

        # Calcular las rutas
        rutas = yen_k_shortest_paths(g_temp, origen, destino, k)
        rutas_encontradas = False
        # Recorrer las rutas. Se analiza las aristas de cada ruta para verificar si se puede enrutar la demanda por esa ruta
        for ruta in rutas:
            for u, v in zip(ruta, ruta[1:]):
                if g_temp.get_capacidad_arista(u, v) >= demanda: 
                    enrutable = True
                    continue     # Se puede enrutar por esta arista, verificar la siguiente arista de la ruta
                else:
                    enrutable = False
                    break # No se puede enrutar por esta ruta, intentar la siguiente ruta
                    
            # Enrutar por la ruta si es enrutable, actualizar la capacidad restante en el diccionario
            if enrutable:
                for u, v in zip(ruta, ruta[1:]): 
                    capacidad_arista = g_temp.get_capacidad_arista(u, v)
                    g_temp.update_capacidad_arista(u, v, capacidad_arista - demanda)

                #print(f"Demanda de {origen} a {destino}: {demanda} enrutable por la ruta: {' -> '.join(ruta)}")
                #print(f"Capacidad disponible actualizada")
                rutas_encontradas = True
                rutas_guardadas[(origen, destino)] = ruta  # Guardar la ruta por la que se enruta esta demanda
                #g_temp.mostrar_matriz_capacidades()
                break # Se enruta por la primera ruta enrutable encontrada, no se analizan las siguientes rutas
                        
        if not rutas_encontradas:
            exito = False
            break # No se pudo enrutar la demanda por ninguna de las rutas encontradas, se termina el proceso de enrutar

    print("\n" + "="*60)
    if exito:
        print(f"Se han enrutado todas las demandas")
    else:
        print(f"No se han podido enrutar todas las demandas")
    print("="*60 + "\n")

    return rutas_guardadas, exito

def calcular_accesibilidad(grafo, ruta):
    """
    Calcula la probabilidad de que el paquete llegue desde el nodo inicial al nodo final a través de la ruta dada
        
    Argumentos:
        grafo (Grafo): El grafo que contiene las probabilidades de pérdida en sus aristas.
        ruta (list): Lista que representa la ruta para la cual se desea calcular la accesibilidad.
    """
    probabilidad_total = 1  # Inicializar a 1
    # Recorrer la ruta y multiplicar las probabilidades de pérdida de cada arista
    for i in range(len(ruta) - 1):
        origen = ruta[i]
        siguiente = ruta[i + 1]

        if siguiente in grafo.grafo[origen]:
            probabilidad_perdida = grafo.get_probabilidad_perdida(origen, siguiente)  # Obtener la probabilidad de pérdida de la arista entre origen y siguiente
            probabilidad_total *= (1 - probabilidad_perdida)  # Multiplicar la probabilidad de éxito (1 - probabilidad de pérdida)
        else:
            break  # Si no hay enlace entre origen y siguiente, se detiene el cálculo
            
    return probabilidad_total
    
def calculo_retardo(ruta, nodo_TA, m, n):
    """
    Calcula el retardo total de una ruta dada en el grafo. El retardo para cada arista se asume como 1ms, equivalente al número de saltos. 

    Argumentos:
        ruta (list): Lista que representa la ruta para la cual se desea calcular el retardo.
        nodo_TA (str): Nodo TA seleccionado en la ruta.
        m (int): Número de veces que se ha perdido el paquete antes de llegar al TA
        n (int): Número de veces que se ha perdido el paquete después de llegar al TA

    Returns:
        float: Retardo total de la ruta. Si la ruta no es válida, devuelve float('inf').
    """
    retardo_total = 0
    tiempo_ida = len(ruta) - 1  # El retardo de ida se asume como el número de saltos 
    tiempo_ida_vuelta = tiempo_ida * 2          # Se asume que es lo mismo al ser la misma ruta: (δs,d + ¯δd,s)

    ruta_desde_TA = ruta[ruta.index(nodo_TA) : ]  # Obtener la subruta desde el TA hasta el nodo de destino
    tiempo_ida_TA = len(ruta_desde_TA) - 1  
    tiempo_ida_vuelta_TA = tiempo_ida_TA * 2          # Se asume que es lo mismo al ser la misma ruta: (δd,s + ¯δs,d)

    retardo_total = (m * tiempo_ida_vuelta) + (n * tiempo_ida_vuelta_TA) + tiempo_ida

    return retardo_total

def calculo_EPDD(grafo, ruta, nodo_TA, m, n):
    """
    Calcula el EPDD de una ruta dada en el grafo.

    Argumentos:
        grafo (Grafo): El grafo que contiene las probabilidades de pérdida en sus aristas.
        ruta (list): Lista que representa la ruta para la cual se desea calcular el EPDD.
        nodo_TA (str): Nodo TA seleccionado en la ruta.
        m (int): Número de veces que se ha perdido el paquete antes de llegar al TA
        n (int): Número de veces que se ha perdido el paquete después de llegar al TA

    Returns:
        float: EPDD total de la ruta. 
    """
    epdd = 0

    accesibilidad_hasta_TA = calcular_accesibilidad(grafo, ruta[:ruta.index(nodo_TA) + 1])  # Accesibilidad desde el nodo de origen hasta el TA
    accesibilidad_desde_TA = calcular_accesibilidad(grafo, ruta[ruta.index(nodo_TA) : ])  # Accesibilidad desde el TA hasta el nodo de destino
    
    #print(f"   [Debug] Accesibilidad al TA: {accesibilidad_hasta_TA}")
    #print(f"   [Debug] Accesibilidad desde el TA: {accesibilidad_desde_TA}")

    for i in range(m):
        for j in range(n):
            if accesibilidad_hasta_TA == 1.0 and accesibilidad_desde_TA == 1.0:
                proba_perdida = 0
            else:
                proba_perdida = ((1 - accesibilidad_hasta_TA) ** i) * accesibilidad_hasta_TA * ((1 - accesibilidad_desde_TA) ** j) * accesibilidad_desde_TA

            retardo = calculo_retardo(ruta, nodo_TA, i, j)

            epdd = epdd + (proba_perdida * retardo)

    return epdd