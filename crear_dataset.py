import csv
import random
from src.funciones import enrutar, calculo_EPDD, calculo_EPDD_optimo
import src.clase_grafo as g
import src.clase_trafico as t

def generar_dataset():
    """
    Genera el daatset con las diferenntes opciones donde poner el nodo TA.

    Topología: Abilene, Geant, Germany, Nobel                            (1, 2, 3, 4)
    Tráfico: TM1, TM2, TM3, TM4, TM5                                     (TM1, TM2, TM3, TM4, TM5)
    Probabilidad de pérdida: 10% o aleatoria entre 0% y 10%              (1, 2)
    Delay: 1ms o aleatorio entre 1ms y 10ms                              (1, 2)
    Nodo TA: nodo con menor EPDD en la ruta entre el primer nodo y el último nodo elegido por el usuario
    """
    #Crear el archivo CSV
    with (open('Abilene.csv', mode='w', newline='') as file_csv,
        open('Consola.txt', mode='w', encoding='utf-8') as file_txt):

        writer = csv.writer(file_csv)
        writer_txt = file_txt.write

        #Generar el grafo de Abilene
        grafo = g.Grafo()
        grafo.cargar_desde_archivo("Abilene")

        nodos = list(grafo.grafo.keys())        #Obtener la lista de nodos del grafo para elegir el nodo TA
        total_nodos = len(nodos) * len(nodos)   #Número total de nodos
        
        cabecera = ['Topologia'] + ['id'] * total_nodos + ['Prob_perdida', 'Delay', 'Nodo_TA']
        
        writer.writerow(cabecera) #Escribir la cabecera del dataset 

        #Lista para guardar el TA de cada ruta y las veces que se repite cada TA
        lista_TA = []
        
        #Utilizar las distintas tologías
        for tm in ['TM1', 'TM2', 'TM3', 'TM4', 'TM5']:
            file_txt.write(f"\nProcesando {tm} en Abilene...\n")
            print(f"Procesando {tm} en Abilene...")

            #Cargar la matriz de tráfico para la topología Abilene y el tráfico TM
            trafico = t.Trafico()
            trafico.cargar_matriz_trafico("Abilene", tm)

            #Comprimir la matriz de tráfico 
            valores_trafico = []
            for fila in trafico.matriz_trafico:
                for valor in fila:
                    valores_trafico.append(valor)

            
            for probabilidad in range (1, 3):  # 1 para 10% y 2 para aleatoria
                print(f"  Probabilidad de pérdida: {'10%' if probabilidad == 1 else 'aleatoria entre 0% y 10%'}")
                file_txt.write(f"  Probabilidad de pérdida: {'10%' if probabilidad == 1 else 'aleatoria entre 0% y 10%'}\n")
                
                for delay in range (1, 3):  # 1 para 1ms y 2 para aleatoria
                    print(f"    Delay: {'1ms' if delay == 1 else 'aleatorio entre 1ms y 10ms'}")
                    file_txt.write(f"    Delay: {'1ms' if delay == 1 else 'aleatorio entre 1ms y 10ms'}\n")

                    for origen in grafo.grafo:
                        for destino in grafo.grafo[origen]:
                            prob_grafo = 0.10 if probabilidad == 1 else round(random.uniform(0.0, 0.1), 2)
                            delay_grafo = 1 if delay == 1 else round(random.uniform(1, 10), 2)

                            grafo.set_probabilidad_perdida(origen, destino, prob_grafo)
                            grafo.set_delay(origen, destino, delay_grafo)

                    #Realizar el enturamiento para obtener las rutas (Recordar que el enrutamiento se hace con el número de saltos, no con el delay ni la probabilidad de pérdida)
                    rutas, exito = enrutar(grafo, trafico, k=36)
                    
                    #Si no se puede enrutar, no se escribe nada en el dataset
                    if exito:
                        lista_TA = []  # Reiniciar la lista de TA para cada combinación de probabilidad y delay
                        file_txt.write("      --- Detalle de rutas ---\n")
                        for ruta in rutas.values():
                            #Calcular el EPDD óptimo para cada ruta
                            nodo_TA_optimo, epdd_optimo = calculo_EPDD_optimo(grafo, ruta, 100, 100)
                            
                            lista_TA.append(nodo_TA_optimo) #Añadir el nodo TA óptimo a la lista de TA

                            file_txt.write(f"        Ruta {ruta} -> Mejor TA local: {nodo_TA_optimo} (EPDD: {epdd_optimo})\n")
                        file_txt.write("      ------------------------\n")
                        #Obtener el nodo TA que más se repite en la lista
                        nodo_TA_optimo_global = max(set(lista_TA), key=lista_TA.count)

                        TAs = {n: lista_TA.count(n) for n in set(lista_TA)}
                        TAs_ordenados = dict(sorted(TAs.items(), key=lambda item: item[1], reverse=True))
                        file_txt.write(f"      Frecuencias en este escenario: {TAs_ordenados} | Optimo: {nodo_TA_optimo_global}\n")

                        #Escribir la información en el dataset
                        fila_datos = [1] + valores_trafico + [prob_grafo, delay_grafo, nodo_TA_optimo_global]   # 1 porque es Abilene
                        writer.writerow(fila_datos)
                           
if __name__ == "__main__":
    generar_dataset()