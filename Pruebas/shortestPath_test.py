from src.clase_grafo import Grafo
from src.funciones import *

def ejecutar_k_shortest_paths(grafo, origen, destino, k, tipo_enrutamiento = 1):
    
    print(f"\n{'='*60}")
    print(f"PRUEBA: Algoritmo de los {k} mejores caminos (Yen's K-Shortest Paths)")
    print(f"Buscando los {k} mejores caminos de {origen} a {destino}")
    print(f"{'-'*60}")

    grafo.mostrar_diccionario()

    rutas = yen_k_shortest_paths(grafo, origen, destino, k, tipo_enrutamiento = tipo_enrutamiento)
    if not rutas:
        print(f"No se encontraron rutas de {origen} a {destino}.")
        return
    
    for i, ruta in enumerate(rutas):
        coste = calcular_coste_ruta(grafo.grafo, ruta)
        print(f"Ruta {i + 1}: {' -> '.join(ruta)} | Coste total: {coste}")
    

# ---------------------------------------------------------------------------------------------
# CASO 1. Resultado esperado: El mejor camino es S -> B -> T con coste 10
# ---------------------------------------------------------------------------------------------
def caso1_shortest_paths():
    grafo = Grafo()
    
    grafo.agregar_arista('S', 'A', 10) 
    grafo.agregar_arista('A', 'S', 50) 
    
    grafo.agregar_arista('A', 'T', 10)
    grafo.agregar_arista('T', 'A', 50)

    grafo.agregar_arista('S', 'B', 5)
    grafo.agregar_arista('B', 'S', 50)
    
    grafo.agregar_arista('B', 'T', 5)
    grafo.agregar_arista('T', 'B', 50)

    grafo.agregar_arista('S', 'T', 100)
    grafo.agregar_arista('T', 'S', 100)
    
    ejecutar_k_shortest_paths(grafo, 'S', 'T', k=3, tipo_enrutamiento=1)

# ---------------------------------------------------------------------------------------------
# CASO 2. Resultado esperado: El mejor camino es A -> B -> C con coste 2
# ---------------------------------------------------------------------------------------------
def caso2_shortest_paths():
    grafo = Grafo()
    
    grafo.agregar_arista('A', 'B', 1)   
    grafo.agregar_arista('B', 'A', 100) 
    
    grafo.agregar_arista('B', 'C', 1)
    grafo.agregar_arista('C', 'B', 100)

    grafo.agregar_arista('A', 'C', 10)
    grafo.agregar_arista('C', 'A', 10)
    
    ejecutar_k_shortest_paths(grafo, 'A', 'C', k=2, tipo_enrutamiento=1)

# ---------------------------------------------------------------------------------------------
# CASO 3. Resultado esperado: El mejor camino es S -> A -> B -> D -> E -> T con coste 23
# ---------------------------------------------------------------------------------------------
def caso3_shortest_paths():
    grafo = Grafo()
    
    grafo.agregar_arista('S', 'A', 5);  grafo.agregar_arista('A', 'S', 5)
    grafo.agregar_arista('S', 'B', 10); grafo.agregar_arista('B', 'S', 10)
    grafo.agregar_arista('S', 'C', 15); grafo.agregar_arista('C', 'S', 15)
    
    grafo.agregar_arista('A', 'B', 2); grafo.agregar_arista('B', 'A', 2)
    
    grafo.agregar_arista('A', 'D', 10); grafo.agregar_arista('D', 'A', 10)
    grafo.agregar_arista('B', 'D', 5);  grafo.agregar_arista('D', 'B', 5)
    grafo.agregar_arista('C', 'E', 5);  grafo.agregar_arista('E', 'C', 5)
    
    grafo.agregar_arista('D', 'E', 1);  grafo.agregar_arista('E', 'D', 1)
    
    grafo.agregar_arista('D', 'T', 10); grafo.agregar_arista('T', 'D', 10)
    grafo.agregar_arista('E', 'T', 10); grafo.agregar_arista('T', 'E', 10)
    
    ejecutar_k_shortest_paths(grafo, 'S', 'T', k=5, tipo_enrutamiento=1)

