from src.funciones import mapeo_letra

class Trafico:
    def __init__(self):
        self.matriz_trafico = []    # Matriz de tráfico (lista de listas)
        self.dicc_restante = {}   # Diccionario para almacenar la matriz restante del tráfico
        self.lista_demandas = []     # Lista para almacenar las demandas en orden

    def cargar_matriz_trafico(self, nombre_topologia, id_trafico, id = None):
        """
        Carga la matriz de tráfico desde un archivo CSV.

        Argumentos:
            nombre_topologia (str): Nombre de la topología elegida.
            id_trafico (str): Identificador del archivo de tráfico (TM1-TM5).
            id (str, opcional): Identificador de la prueba (si se está cargando desde la carpeta Pruebas). Por defecto es None.
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
            for v, atributos in vecinos.items():
                self.dicc_restante[u][v] = atributos['capacidad']
    
    def get_capacidad_restante(self, origen, destino):
        """ 
        Obtiene la capacidad restante entre dos nodos. 
            Argumentos: 
                origen (str): Nodo de origen. 
                destino (str): Nodo de destino. 
            Retorna: 
                float: Capacidad restante entre el nodo de origen y el nodo de destino. 
        """ 
        return self.dicc_restante.get(origen, {}).get(destino, 0)
    
    def ordenar_capacidad(self):
        """
        Ordena el diccionario de tráfico restante por capacidad de mayor a menor dentro de una lista de vectores. 
        """
        self.lista_demandas = [] # Limpiar la lista de demandas antes de ordenarla

        for i in range(len(self.matriz_trafico)):
            for j in range(len(self.matriz_trafico[i])):
                demanda = self.matriz_trafico[i][j]                 #Obtener la demanda de la matriz de tráfico

                if demanda > 0:                             
                    origen = mapeo_letra(i)
                    destino = mapeo_letra(j)

                    origen_destino = [origen, destino]              # Vector que guarda el nodo de origen y el nodo de destino
                    
                    self.lista_demandas.append((demanda, origen_destino))   # Agregar la demanda y el vector de origen-destino a la lista de demandas
                
        # Ordenar la lista de demandas por demanda de mayor a menor
        self.lista_demandas.sort(key=lambda x: x[0], reverse=True)

    def mayor_demanda(self):
        """
        Obtiene, devuelve y elimina la demanda más alta de la lista (la primera).        
        Retorna:
            tuple: (demanda, [origen, destino]) o None si la lista ya está vacía.
        """
        if len(self.lista_demandas) > 0:
            return self.lista_demandas.pop(0)
        else:
            return None  # Ya no quedan demandas por procesar
        
    def actualizar_matriz_restante(self, origen, destino, demanda):
        """
        Actualiza la matriz restante del tráfico después de enrutar una demanda.

        Argumentos:
            origen (str): Nodo de origen.
            destino (str): Nodo de destino.
            demanda (float): Cantidad de tráfico que se ha enrutable por la ruta seleccionada.
        """
        if origen in self.dicc_restante and destino in self.dicc_restante[origen]:
            self.dicc_restante[origen][destino] -= demanda
        
    def mostrar_matriz_trafico(self):
        """
        Muestra la matriz de tráfico cargada en forma de tabla 2D.
        """
        print("\nMatriz de Tráfico Cargada:")
        
        if not self.matriz_trafico:
            print("La matriz está vacía.")
            return

        num_nodos = len(self.matriz_trafico)
        # Generar las letras para los nodos (A, B, C, D...) automáticamente
        nodos = [mapeo_letra(i) for i in range(num_nodos)]
        
        ancho = 8  
        
        # 1. Imprimir el encabezado de las columnas
        encabezado = "    " + "".join([f"{nodo:>{ancho}}" for nodo in nodos])
        print(encabezado)
        
        # 2. Imprimir cada fila con su letra y sus valores
        for i in range(num_nodos):
            fila_str = f"{nodos[i]:<3} " # Letra de la fila (ej: "A  ")
            
            for j in range(num_nodos):
                valor = self.matriz_trafico[i][j]
                # Formatear el número para que ocupe el ancho especificado
                fila_str += f"{valor:>{ancho}.1f}"
                
            print(fila_str)
        print("") # Salto de línea extra al final para que quede limpio

    def mostrar_matriz_restante(self):
        """
        Muestra la matriz restante del tráfico en forma de tablas
        """
        print("\nMatriz Restante del Tráfico:")
        for origen, destinos in self.dicc_restante.items():
            print (f"{origen}: {destinos}")
