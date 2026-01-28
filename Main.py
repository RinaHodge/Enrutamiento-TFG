import Menus
import ClaseGrafo as g
import ClaseTrafico as t


grafo = g.Grafo()       #Crear instancia del grafo
trafico = t.Trafico()   #Crear instancia del tráfico

nombre, id_trafico = Menus.menu_inicial()   #Llama al menú inicial para seleccionar topología y tráfico

# Cargar la topología y mostrar el grafo cargado
grafo.cargar_desde_archivo(nombre)
grafo.mostrar_diccionario()

# Cargar la matriz de tráfico y mostrarla
trafico.cargar_matriz_trafico(nombre, id_trafico)
trafico.mostrar_matriz_trafico()

# Aplicar el algoritmo de encaminamiento (Dijkstra)
