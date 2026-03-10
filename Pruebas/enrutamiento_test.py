from src.clase_grafo import Grafo
from src.funciones import *
from src.clase_trafico import Trafico

grafo1 = Grafo()
    
grafo1.agregar_arista('A', 'B', 10) 
grafo1.agregar_arista('B', 'A', 50) 
    
grafo1.agregar_arista('B', 'D', 10)
grafo1.agregar_arista('D', 'B', 50)

grafo1.agregar_arista('A', 'C', 5)
grafo1.agregar_arista('C', 'A', 50)
    
grafo1.agregar_arista('C', 'D', 5)
grafo1.agregar_arista('D', 'C', 50)

grafo1.agregar_arista('A', 'D', 100)
grafo1.agregar_arista('D', 'A', 100)

def caso1_enrutamiento():

    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM1", id = 1)

    print("Caso 1: Enrutamiento con grafo1 y TM1")
    
    print("Matriz de tráfico original:")
    trafico.mostrar_matriz_trafico()
    
    enrutar(grafo1, trafico, k = 3)

def caso2_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM2", id = 1)

    print("Caso 2: Enrutamiento con grafo1 y TM2")
    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5)

def caso3_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM3", id = 1)

    print("Caso 3: Enrutamiento con grafo1 y TM3")
    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5)

def caso4_enrutamiento(): 
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM4", id = 1)

    print("Caso 4: Enrutamiento con grafo1 y TM4")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5)

def caso5_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM5", id = 1)

    print("Caso 5: Enrutamiento con grafo1 y TM5")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5)

def caso6_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM6", id = 1)

    print("Caso 6: Enrutamiento con grafo1 y TM6")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5)