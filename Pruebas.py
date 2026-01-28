import random
import ClaseGrafo as g
import Funciones as f

def generarGrafo(): 
    """
    Genera un grafo de ejemplo con aristas y costes aleatorios.
    Returns:
        Grafo: Instancia de la clase Grafo con aristas agregadas.
    """
    grafo = g.Grafo()       #Crear instancia del grafo

    grafo.agregar_arista('A', 'B', random.randint(1,10))
    grafo.agregar_arista('A', 'C', random.randint(1,10))
    grafo.agregar_arista('B', 'C', random.randint(1,10))
    grafo.agregar_arista('B', 'D', random.randint(1,10))
    grafo.agregar_arista('C', 'D', random.randint(1,10))
    return grafo

def probarDijkstra():
    """
    Prueba el algoritmo de Dijkstra en un grafo de ejemplo.
    """
    print("Probando Dijkstra en un grafo de ejemplo:")
    grafo = generarGrafo()
    grafo.mostrar_diccionario()

    nodo_inicio = 'A'
    dist, prev = f.Dijkstra(grafo.grafo, nodo_inicio)

    print(f"Distancias desde el nodo {nodo_inicio}:")
    for nodo in dist:
        print(f"Distancia a {nodo}: {dist[nodo]}")

    print(f"Predecesores en las rutas más cortas desde {nodo_inicio}:")
    for nodo in prev:
        print(f"Predecesor de {nodo}: {prev[nodo]}")

    # Reconstruir y mostrar la ruta más corta desde A a D
    print("Reconstruyendo la ruta más corta desde A hasta D:")
    ruta = f.reconstruir_ruta(prev, 'A', 'D')
    print("Ruta más corta de A a D:", " -> ".join(ruta))