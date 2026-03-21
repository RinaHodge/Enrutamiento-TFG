from src.funciones import enrutar
import src.menus as menus
import src.clase_grafo as g
import src.clase_trafico as t

grafo = g.Grafo()       #Crear instancia del grafo
trafico = t.Trafico()   #Crear instancia del tráfico

nombre, id_trafico = menus.menu_inicial()   #Llama al menú inicial para seleccionar topología y tráfico

if nombre is None and id_trafico is None:
    print("No se seleccionó ninguna topología. Saliendo del programa.")
    exit()

# Cargar la topología y mostrar el grafo cargado
grafo.cargar_desde_archivo(nombre)
grafo.mostrar_diccionario()

# Cargar la matriz de tráfico y mostrarla
trafico.cargar_matriz_trafico(nombre, id_trafico)
trafico.mostrar_matriz_trafico()


# Agregar pérdida a los enlaces (opcional, se puede comentar si no se desea agregar pérdida)
for origen in grafo.grafo:
    for destino in grafo.grafo[origen]:
        probabilidad = 1  # Puedes cambiar este valor por el que necesites 
        grafo.set_probabilidad_perdida(origen, destino, probabilidad)

print("\nGrafo con la probabilidad de pérdida establecida:")
grafo.mostrar_diccionario()  # Mostrar el grafo con la probabilidad de pérdida establecida

#Con 40 caminos funciona germany hasta TM3
#enrutar(grafo, trafico, k = 36)   #Llama a la función de enrutamiento con k=3. Con 700 caminos no funciona

