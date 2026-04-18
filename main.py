from src.funciones import enrutar, calculo_EPDD, calculo_EPDD_optimo
import random
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

probabilidad_perdida = menus.menu_proba_perdida()

if probabilidad_perdida == 1:
    print("\nHa seleccionado establecer una probabilidad de pérdida para las aristas.")
else: 
    print("\nHa seleccionado establecer una probabilidad de pérdida aleatoria para las aristas.")

for origen in grafo.grafo:
    for destino in grafo.grafo[origen]:
        if probabilidad_perdida == 1:
            probabilidad = 0.05 # probabilidad de perdida del 5%
        else:
            probabilidad = round(random.uniform(0.0, 0.1), 2)  # Generar una probabilidad de pérdida aleatoria entre 0% y 10%
        grafo.set_probabilidad_perdida(origen, destino, probabilidad)

print("\nGrafo con la probabilidad de pérdida establecida:")
grafo.mostrar_diccionario()  # Mostrar el grafo con la probabilidad de pérdida establecida

#Con 40 caminos funciona germany hasta TM3
rutas_guardadas, exito = enrutar(grafo, trafico, k = 36)   # Llama a la función de enrutamiento con k=3. Con 700 caminos no funciona

epdd_elegido = menus.menu_epdd()
nodos_disponibles = list(grafo.grafo.keys())
primer_nodo, ultimo_nodo = menus.menu_eleccion_ruta(nodos_disponibles)
ruta_explorar = rutas_guardadas.get((primer_nodo, ultimo_nodo), None)  # Obtener la ruta guardada para ir del primer nodo al último nodo

if epdd_elegido == 0:
    print("\nNo se ha seleccionado ningún EPDD. Saliendo del programa.")
    exit()
elif epdd_elegido == 1:
    print("\nEPDD seleccionado: EPDD aleatorio.")

    if ruta_explorar is not None:
        print(f"\nRuta a usar para ir del nodo {primer_nodo} al nodo {ultimo_nodo}: {' -> '.join(ruta_explorar)}")
   
        nodo_TA = random.choice(ruta_explorar)  # Seleccionar aleatoriamente un nodo TA de la ruta encontrada
        print(f"Nodo TA seleccionado aleatoriamente en: {nodo_TA}")

        calculo_EPDD = calculo_EPDD(grafo, ruta_explorar, nodo_TA, 100, 100)  # Calcular el EPDD con el nodo TA seleccionado
        print(f"EPDD calculado con TA en el nodo {nodo_TA}: {calculo_EPDD}")
    else:
        print(f"\nNo se encontró una ruta guardada para ir de {primer_nodo} a {ultimo_nodo}.")
else:
    print("\nEPDD seleccionado: EPDD con menor probabilidad de pérdida.")

    if ruta_explorar is not None:
        print(f"\nRuta a usar para ir del nodo {primer_nodo} al nodo {ultimo_nodo}: {' -> '.join(ruta_explorar)}")
   
        nodo_TA_optimo, epdd_optimo = calculo_EPDD_optimo(grafo, ruta_explorar, 100, 100)  # Calcular el nodo TA óptimo para minimizar la probabilidad de pérdida
        print(f"Nodo TA óptimo seleccionado: {nodo_TA_optimo}")
        print(f"EPDD óptimo calculado: {epdd_optimo}")






