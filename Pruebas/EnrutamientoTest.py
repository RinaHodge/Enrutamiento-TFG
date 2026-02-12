import ClaseGrafo as g
import ClaseTrafico as t
import Funciones as f

grafo1 = g.Grafo()
    
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

    trafico = t.Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM1", id = 1)

    print("Caso 1: Enrutamiento con grafo1 y TM1")
    
    print("Matriz de tráfico original:")
    trafico.mostrar_matriz_trafico()
    
    print("Matriz restante del tráfico:")
    trafico.mostrar_matriz_restante()
    
    f.enrutar(grafo1, trafico, k = 3)