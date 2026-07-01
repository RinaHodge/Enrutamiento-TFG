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

enrutamiento_elegido = menus.menu_enrutamiento()
if enrutamiento_elegido == 0:
    print("Saliendo del programa.")
    exit()

# Cargar la topología y mostrar el grafo cargado
grafo.cargar_desde_archivo(nombre)
grafo.mostrar_diccionario()

# Cargar la matriz de tráfico y mostrarla
trafico.cargar_matriz_trafico(nombre, id_trafico)
trafico.mostrar_matriz_trafico()

# -----------------------------------------------------------------------------------------------------------
#                       PROBABILIDAD DE PÉRDIDA Y DELAY EN LAS ARISTAS DEL GRAFO
# -----------------------------------------------------------------------------------------------------------
probabilidad_perdida = menus.menu_proba_perdida()
delay_elegido = menus.menu_delay()

# Si intenta usar el CSV de delays reales pero NO está en Abilene, le avisamos y forzamos el modo aleatorio
if enrutamiento_elegido == 2 and delay_elegido == 1 and nombre != "Abilene":
    print(f"\nAVISO: Los datos de delay reales (CSV) solo están disponibles para la topología Abilene.")
    print(f"Como ha seleccionado {nombre}, se aplicarán delays aleatorios (1-10ms) para que la red funcione.")
    delay_elegido = 2  # Forzamos a que genere los aleatorios y no busque el CSV

if probabilidad_perdida == 1:
    print("\nHa seleccionado establecer una probabilidad de pérdida por defecto para las aristas.")
elif probabilidad_perdida == 2:
    print("\nHa seleccionado establecer una probabilidad de pérdida aleatoria para las aristas.")

if delay_elegido == 1:
    print("\nHa seleccionado establecer un delay predeterminado (1ms) para las aristas.")
elif delay_elegido == 2:
    print("\nHa seleccionado establecer un delay aleatorio (1ms-10ms) para las aristas.")

for origen in grafo.grafo:
    for destino in grafo.grafo[origen]:
        if probabilidad_perdida == 1:
            probabilidad = 0.1 # probabilidad de perdida del 10%
        else:
            probabilidad = round(random.uniform(0.0, 0.1), 2)  # Generar una probabilidad de pérdida aleatoria entre 0% y 10%
        grafo.set_probabilidad_perdida(origen, destino, probabilidad)

        #Establcer el delay
        if (enrutamiento_elegido == 1 and delay_elegido == 1):
            delay = 1 # delay predeterminado de 1ms
            grafo.set_delay(origen, destino, delay)
        elif (delay_elegido == 2):
            delay = random.randint(1, 10)  # Generar un delay aleatorio entre 1ms y 10ms
            grafo.set_delay(origen, destino, delay)

if(enrutamiento_elegido == 2 and delay_elegido == 1 and nombre == "Abilene"):
    ruta_abilene = f"delay_topologias/delay_Abilene.csv"
    try: 
        with open(ruta_abilene, 'r') as archivo:
            lineas = archivo.readlines()        
            #Procesar las líneas para construir la matriz de capacidades
            for i, linea in enumerate(lineas):              #Procesar la fila
                valores = linea.strip().split(',')

                for j, valor in enumerate(valores):         #Procesar la columna
                    delay = float(valor)

                    #Si la capacidad es mayor que 0, agregar la arista al grafo. Si es menor, no hay enlace
                    if delay > 0:
                        nodo_origen = f"S{i + 1}"
                        nodo_destino = f"S{j + 1}"
                        grafo.set_delay(nodo_origen, nodo_destino, delay)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de delay en la ruta: {ruta_abilene}")


print("\nGrafo con la probabilidad de pérdida y delay establecidos:")

grafo.mostrar_diccionario()  # Mostrar el grafo con la probabilidad de pérdida y delay establecidos

#Con 40 caminos funciona germany hasta TM3
rutas_guardadas, exito = enrutar(grafo, trafico, k = 36, tipo_enrutamiento = enrutamiento_elegido)   # Llama a la función de enrutamiento con k=3. Con 700 caminos no funciona

# ------------------------------------------------------------------------------------------------------------
#                      SELECCIÓN DE EPDD Y NODO TA PARA CALCULAR EL EPDD
# -------------------------------------------------------------------------------------------------------------

print("\n" + "="*60)
print("             SELECCIÓN DEL MODO DE ANÁLISIS DE EPDD")
print("="*60)
print(" 1 -> Analizar un FLUJO ESPECÍFICO (Individual: manual o calculado por el simulador)")
print(" 2 -> Calcular el NODO TA ÓPTIMO GLOBAL para toda la red")
print("-" * 60)
modo_analisis = input("Seleccione una opción (1 o 2): ").strip()

if modo_analisis == "2":
    if exito and rutas_guardadas:
        lista_TA_global = []    #Se va a guarar el nodo TA óptimo de cada ruta para 
        
        # Recorrer todas las rutas enrutadas de la red entera
        for (origen, destino), ruta in rutas_guardadas.items():
            nodo_TA_optimo, epdd_optimo = calculo_EPDD_optimo(grafo, ruta, 100, 100)
            lista_TA_global.append(nodo_TA_optimo)
        
        nodo_TA_optimo_global = max(set(lista_TA_global), key=lista_TA_global.count)
        
        #Mostrar las frecuencias de cada nodo
        frecuencias = {nodo: lista_TA_global.count(nodo) for nodo in set(lista_TA_global)}
        frecuencias_ordenadas = dict(sorted(frecuencias.items(), key=lambda item: item[1], reverse=True))
        
        print(f" El Nodo TA óptimo para TODA la red es: {nodo_TA_optimo_global}")
        print("Votos por nodo:")
        print("-" * 70)
        for nodo, votos in frecuencias_ordenadas.items():
            porcentaje = (votos / len(lista_TA_global)) * 100
            print(f"   • Nodo {nodo:<4} : {votos:>3} flujos lo eligieron ({porcentaje:.1f}%)")
        print("-" * 70)
    else:
        print("❌ Error: No se puede realizar el análisis global porque el enrutamiento falló.")
else:
    print("¿Desea usar la ruta calculada por el simulador o forzar una manual?")
    print(" -> Pulse ENTER para usar la calculada.")
    print(" -> O escriba los nodos separados por comas para forzarla (Ej: S1,S2,S5,S7,S4,S11)")
    nodos_disponibles = list(grafo.grafo.keys())
    print(f"Nodos disponibles en la red: {', '.join(nodos_disponibles)}")
    ruta_manual = input("Ruta manual (o ENTER): ").strip()

    epdd_elegido = menus.menu_epdd()

    if ruta_manual:
        # Convertimos el texto introducido en una lista de nodos limpiando los espacios
        ruta_explorar = [nodo.strip() for nodo in ruta_manual.split(',')]
        # Actualizamos el primer y último nodo por si cambiaste los extremos en tu ruta manual
        primer_nodo = ruta_explorar[0]
        ultimo_nodo = ruta_explorar[-1]
        print(f"\n****Se ha forzado la ruta manual para pruebas.****")
    else: 
        primer_nodo, ultimo_nodo = menus.menu_eleccion_ruta(nodos_disponibles)
        ruta_explorar = rutas_guardadas.get((primer_nodo, ultimo_nodo), None)  # Obtener la ruta guardada para ir del primer nodo al último nodo

    if epdd_elegido == 0:
        print("\nNo se ha seleccionado ningún EPDD. Saliendo del programa.")
        exit()
    elif epdd_elegido == 1:
        print("\nEPDD seleccionado: EPDD aleatorio. (Selecciona un nodo TA aleatorio de la ruta encontrada para calcular el EPDD).")

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
            print(f"\nRuta a usada para ir del nodo {primer_nodo} al nodo {ultimo_nodo}: {' -> '.join(ruta_explorar)}")






