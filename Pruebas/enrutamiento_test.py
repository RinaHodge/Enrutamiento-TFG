from src.clase_grafo import Grafo
from src.funciones import *
from src.clase_trafico import Trafico
import random, os

grafo1 = Grafo()
    
grafo1.agregar_arista('S1', 'S2', 10) 
grafo1.agregar_arista('S2', 'S1', 50) 
    
grafo1.agregar_arista('S2', 'S4', 10)
grafo1.agregar_arista('S4', 'S2', 50)

grafo1.agregar_arista('S1', 'S3', 5)
grafo1.agregar_arista('S3', 'S1', 50)
    
grafo1.agregar_arista('S3', 'S4', 5)
grafo1.agregar_arista('S4', 'S3', 50)

grafo1.agregar_arista('S1', 'S4', 100)
grafo1.agregar_arista('S4', 'S1', 100)


grafo2 = Grafo()

grafo2.agregar_arista('S1', 'S2', 70) 
grafo2.agregar_arista('S2', 'S1', 30) 
    
grafo2.agregar_arista('S2', 'S5', 60)
grafo2.agregar_arista('S5', 'S2', 20)

grafo2.agregar_arista('S1', 'S3', 40)
grafo2.agregar_arista('S3', 'S1', 60)
    
grafo2.agregar_arista('S3', 'S4', 50)
grafo2.agregar_arista('S4', 'S3', 50)

grafo2.agregar_arista('S4', 'S5', 60)
grafo2.agregar_arista('S5', 'S4', 40)

grafo2.agregar_arista('S1', 'S5', 80) 
grafo2.agregar_arista('S5', 'S1', 100) 


def caso1_enrutamiento():

    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM1", id = 1)

    print("Caso 1: Enrutamiento con grafo1 y TM1")
    
    print("Matriz de tráfico original:")
    trafico.mostrar_matriz_trafico()
    
    enrutar(grafo1, trafico, k = 3, tipo_enrutamiento = 1)   # Llama a la función de enrutamiento con k=3 y enrutamiento por número de saltos

def caso2_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM2", id = 1)

    print("Caso 2: Enrutamiento con grafo1 y TM2")
    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5, tipo_enrutamiento = 1)

def caso3_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM3", id = 1)

    print("Caso 3: Enrutamiento con grafo1 y TM3")
    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5, tipo_enrutamiento = 1)

def caso4_enrutamiento(): 
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM4", id = 1)

    print("Caso 4: Enrutamiento con grafo1 y TM4")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5, tipo_enrutamiento = 1)

def caso5_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM5", id = 1)

    print("Caso 5: Enrutamiento con grafo1 y TM5")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo1, trafico, k = 5, tipo_enrutamiento = 1)

def caso6_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo2", "TM1", id = 2)

    print("Caso 6: Enrutamiento con grafo2 y TM1")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo2, trafico, k = 7, tipo_enrutamiento = 1)

def caso7_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo2", "TM2", id = 2)

    print("Caso 7: Enrutamiento con grafo2 y TM2")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo2, trafico, k = 7, tipo_enrutamiento = 1)

def caso8_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo2", "TM3", id = 2)

    print("Caso 8: Enrutamiento con grafo2 y TM3")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo2, trafico, k = 7, tipo_enrutamiento = 1)

def caso9_enrutamiento():
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo2", "TM4", id = 2)

    print("Caso 9: Enrutamiento con grafo2 y TM4")

    trafico.mostrar_matriz_trafico()

    enrutar(grafo2, trafico, k = 7, tipo_enrutamiento = 1)

def caso_enrutamientoDelay():
    for origen in grafo1.grafo:
        for destino in grafo1.grafo[origen]:
            grafo1.set_delay(origen, destino, 2) 

    for origen in grafo2.grafo:
        for destino in grafo2.grafo[origen]:
            grafo2.set_delay(origen, destino, random.randint(1, 10))

            # --- NUEVO CÓDIGO PARA IMPRIMIR LA MATRIZ DE DELAYS ---
    print("\n" + "-"*40)
    print("MATRIZ DE DELAYS GENERADA (GRAFO 2)")
    print("-" * 40)
    
    nodos_g2 = sorted(list(grafo2.grafo.keys()))
    
    # Imprimir encabezado de columnas
    encabezado = "    " + "".join([f"{nodo:>5}" for nodo in nodos_g2])
    print(encabezado)
    
    # Imprimir cada fila
    for origen in nodos_g2:
        fila_str = f"{origen:<3} "
        for destino in nodos_g2:
            # Buscamos si existe el enlace, si no, ponemos un 0
            if destino in grafo2.grafo[origen]:
                # Dependiendo de cómo lo guardes en tu clase Grafo, usamos .get()
                delay_val = grafo2.grafo[origen][destino].get('delay', 0)
            else:
                delay_val = 0
                
            fila_str += f"{delay_val:>5}"
        print(fila_str)
    print("-" * 40 + "\n")

    #================
    #Grafo 1
    trafico = Trafico()
    trafico.cargar_matriz_trafico("grafo1", "TM1", id = 1)

    print("\n" + "="*50)
    print("Caso 10a: Enrutamiento con grafo1 (Por DELAY)")
    print("="*50)
    
    # tipo_enrutamiento = 2 (Busca la ruta más rápida, no la más corta en saltos)
    rutas_guardadas, exito = enrutar(grafo1, trafico, k = 3, tipo_enrutamiento=2)

    if exito:
        print("-" * 60)
        for (origen, destino), ruta in rutas_guardadas.items():
            camino_formateado = " -> ".join(ruta)
            
            delay_total = sum(grafo1.grafo[u][v].get('delay', 0) for u, v in zip(ruta, ruta[1:]))
            
            print(f"{origen} a {destino}: {camino_formateado:<25} | Delay: {delay_total} ms")
        print("-" * 60)

    #================
    #Grafo 2

    trafico2 = Trafico()
    trafico2.cargar_matriz_trafico("grafo2", "TM1", id = 2)
    print("\n" + "="*60)
    print("Caso 10b: Enrutamiento con grafo2 (DELAY)")
    print("="*60)

    rutas_guardadas2, exito2 = enrutar(grafo2, trafico2, k = 7, tipo_enrutamiento=2)
    if exito2:
        print("-" * 60)
        for (origen, destino), ruta in rutas_guardadas2.items():
            camino_formateado = " -> ".join(ruta)
            
            delay_total = sum(grafo2.grafo[u][v].get('delay', 0) for u, v in zip(ruta, ruta[1:]))
            
            print(f"{origen} a {destino}: {camino_formateado:<25} | Delay: {delay_total} ms")
        print("-" * 60)

    #Mostrar los resultados se ha hechio con ayuda de gemini
def caso_enrutamiento_abilene_real():
    print("\n" + "="*50)
    print("Caso 11: Enrutamiento Abilene con delays reales")
    print("="*50)

    # 1. Cargamos el grafo de Abilene
    grafo_abilene = Grafo()
    grafo_abilene.cargar_desde_archivo("Abilene")

    trafico_abilene = Trafico()
    trafico_abilene.cargar_matriz_trafico("Abilene", "TM1")

    ruta_abilene = "delay_topologias/delay_Abilene.csv" 
    try: 
        with open(ruta_abilene, 'r') as archivo:
            lineas = archivo.readlines()        
            for i, linea in enumerate(lineas):              
                valores = linea.strip().split(',')
                for j, valor in enumerate(valores):         
                    delay = float(valor)
                    if delay > 0:
                        nodo_origen = f"S{i + 1}"
                        nodo_destino = f"S{j + 1}"
                        grafo_abilene.set_delay(nodo_origen, nodo_destino, delay)
    except FileNotFoundError:
        print(f"Error: No se encontró el CSV en {ruta_abilene}. Ajusta la ruta en el test.")
        return

    rutas_guardadas, exito = enrutar(grafo_abilene, trafico_abilene, k = 7, tipo_enrutamiento=2)
    
    if exito: 
        print("-" * 75)
        print(f"{'Origen -> Destino':<20} | {'Ruta Asignada':<35} | {'Delay Total'}")
        print("-" * 75)
        for (origen, destino), ruta in rutas_guardadas.items():
            camino_formateado = " -> ".join(ruta)
            
            # Calculamos el delay total sumando los tramos
            delay_total = sum(grafo_abilene.grafo[u][v].get('delay', 0) for u, v in zip(ruta, ruta[1:]))
            
            print(f"{origen + ' -> ' + destino:<20} | {camino_formateado:<35} | {delay_total:>6.2f} ms")
        print("-" * 75)