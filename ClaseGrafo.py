class Grafo:
    def __init__(self):
        self.grafo = {}         # Diccionario para almacenar los vértices y sus aristas
        self.num_vertices = 0

    def agregar_arista(self, origen, destino, capacidad):
        """
        Agrega una arista al grafo con una capacidad dada.

        Argumentos:
            origen (int): Nodo de origen.
            destino (int): Nodo de destino.
            capacidad (float): Capacidad del enlace entre los nodos.
        """
        if origen not in self.grafo:
            self.grafo[origen] = {}
            self.num_vertices += 1

        self.grafo[origen][destino] = capacidad

    def cargar_desde_archivo(self, nombre_topologia, id_trafico):
        """
        Carga la matriz de capacidades y la matriz de tráfico.

        Argumentos:
            nombre_topologia (str): Nombre de la topología elegida. Proviene del menú inicial.
            id_trafico (str): Identificador del archivo de tráfico (TM1-TM5). Proviene del menú inicial.
        """
        # Implementación para cargar la matriz de capacidades y la matriz de tráfico desde archivos

        ruta_capacidades = f"Topologias/Capacidades/{nombre_topologia}/{nombre_topologia}CapMatrix.csv"
        ruta_trafico = f"Topologias/Matrices_Trafico/{nombre_topologia}/{nombre_topologia}{id_trafico}.csv"

        print (f"Cargando matriz de capacidades desde: {ruta_capacidades}")
        try: 
            with open(ruta_capacidades, 'r') as archivo:
                lineas = archivo.readlines()        

                #Procesar las líneas para construir la matriz de capacidades
                for i, linea in enumerate(lineas):              #Procesar la fila
                    valores = linea.strip().split(',')

                    for j, valor in enumerate(valores):         #Procesar la columna
                        capacidad = float(valor)

                        #Si la capacidad es mayor que 0, agregar la arista al grafo. Si es menor, no hay enlace
                        if capacidad > 0:
                            self.agregar_arista(i, j, capacidad)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo de capacidades en la ruta: {ruta_capacidades}")
        
        print (f"Cargando matriz de tráfico desde: {ruta_trafico}")
        pass

    def mostrar_diccionario(self):
        """
        Muestra el diccionario del grafo.
        """
        for origen in self.grafo:
            for destino in self.grafo[origen]:
                capacidad = self.grafo[origen][destino]
                print(f"Arista desde {origen} hasta {destino} con capacidad {capacidad}")