class Trafico:
    def __init__(self):
        self.matriz_trafico = []    # Matriz de tráfico (lista de listas)
        self.dicc_restante = {}   # Diccionario para almacenar la matriz restante del tráfico

    def cargar_matriz_trafico(self, nombre_topologia, id_trafico, id = None):
        """
        Carga la matriz de tráfico desde un archivo CSV.

        Argumentos:
            nombre_topologia (str): Nombre de la topología elegida.
            id_trafico (str): Identificador del archivo de tráfico (TM1-TM5).
        """

        if id is None:
            ruta_trafico = f"Topologias/Matrices_Trafico/{nombre_topologia}/{nombre_topologia}{id_trafico}.csv"
        else:
            ruta_trafico = f"Pruebas/{nombre_topologia}/{nombre_topologia}{id_trafico}.csv"

        print(f"Cargando matriz de tráfico desde: {ruta_trafico}")
        try:
            with open(ruta_trafico, 'r') as archivo:
                lineas = archivo.readlines()

                self.matriz_trafico = []            #limpiar la matriz antes de cargar una nueva

                for linea in lineas:
                    valores = linea.strip().split(',')
                    fila = [float(valor) for valor in valores]
                    self.matriz_trafico.append(fila)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo de tráfico en la ruta: {ruta_trafico}")
        pass

    def inicializar_dicc_restante(self, grafo):
        """
        Inicializa el diccionario de tráfico restante a partir de la matriz de capacidad y el grafo.
        """
        self.dicc_restante = {}   # Limpiar el diccionario antes de inicializarlo

        for u, vecinos in grafo.grafo.items():
            self.dicc_restante[u] = {}
            for v, capacidad in vecinos.items():
                self.dicc_restante[u][v] = capacidad
    
    def get_capacidad_restante(self, origen, destino):
        """ Obtiene la capacidad restante entre dos nodos. 
            Argumentos: 
                origen (str): Nodo de origen. 
                destino (str): Nodo de destino. 
            Retorna: 
                float: Capacidad restante entre el nodo de origen y el nodo de destino. 
        """ 
        return self.dicc_restante.get(origen, {}).get(destino, 0)
    
    def mostrar_matriz_trafico(self):
        """
        Muestra la matriz de tráfico cargada en forma de tablas
        """
        print("\nMatriz de Tráfico Cargada:")
        for fila in self.matriz_trafico:
            print(fila)

    def mostrar_matriz_restante(self):
        """
        Muestra la matriz restante del tráfico en forma de tablas
        """
        print("\nMatriz Restante del Tráfico:")
        for origen, destinos in self.dicc_restante.items():
            print (f"{origen}: {destinos}")
