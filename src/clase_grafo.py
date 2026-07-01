class Grafo:
    def __init__(self):
        self.grafo = {}         # Diccionario para almacenar los vértices y sus aristas
        self.num_vertices = 0
        self.num_aristas = 0

    def get_num_vertices(self):
        """
        Devuelve el número de vértices en el grafo.

        Returns:
            int: Número de vértices en el grafo.
        """
        return self.num_vertices
    
    def get_num_aristas(self):
        """
        Devuelve el número de aristas en el grafo.

        Returns:
            int: Número de aristas en el grafo.
        """
        return self.num_aristas
    
    def get_capacidad_arista(self,origen, destino):
        """ Devuelve el coste de la arista entre el nodo de origen y el nodo de destino. 
        
            Argumentos: 
                origen (str): Nodo de origen. 
                destino (str): Nodo de destino. 
        
            Returns: float: Coste de la arista entre el nodo de origen y el nodo de destino. Si no existe la arista, devuelve float('inf'). 
        """ 
        if origen in self.grafo and destino in self.grafo[origen]: 
            return self.grafo[origen][destino]['capacidad'] 
        else: 
            return float('inf') # Si no existe la arista, se considera un coste infinito
    
    def get_coste_arista(self, origen, destino):
        """ Devuelve el coste de la arista entre el nodo de origen y el nodo de destino. 
        
            Argumentos: 
                origen (str): Nodo de origen. 
                destino (str): Nodo de destino. 
        
            Returns: float: Coste de la arista entre el nodo de origen y el nodo de destino. Si no existe la arista, devuelve float('inf'). 
        """ 
        if origen in self.grafo and destino in self.grafo[origen]: 
            return self.grafo[origen][destino]['coste'] 
        else: 
            return float('inf') # Si no existe la arista, se considera un coste infinito
    
    def get_probabilidad_perdida(self, origen, destino):
        """ Devuelve la probabilidad de pérdida de la arista entre el nodo de origen y el nodo de destino. 
        
            Argumentos: 
                origen (str): Nodo de origen. 
                destino (str): Nodo de destino. 
        
            Returns: float: Probabilidad de pérdida de la arista entre el nodo de origen y el nodo de destino. Si no existe la arista, devuelve None.
        """ 
        if origen in self.grafo and destino in self.grafo[origen]: 
            return self.grafo[origen][destino].get('prob_perdida', 0.0) 
        else: 
            return None # Si no existe la arista, se considera una probabilidad de pérdida de 0
    
    def get_delay(self, origen, destino):
        """ Devuelve el delay de la arista entre el nodo de origen y el nodo de destino. 
        
            Argumentos: 
                origen (str): Nodo de origen. 
                destino (str): Nodo de destino. 
        
            Returns: float: Delay de la arista entre el nodo de origen y el nodo de destino. Si no existe la arista, devuelve None.
        """ 
        if origen in self.grafo and destino in self.grafo[origen]: 
            return self.grafo[origen][destino].get('delay', 0.0) 
        else: 
            return None # Si no existe la arista, se considera un delay de 0
    
    def update_capacidad_arista(self, origen, destino, nueva_capacidad):
        """ Actualiza la capacidad de la arista entre el nodo de origen y el nodo de destino. 
            Argumentos: 
                origen (str): Nodo de origen. 
                destino (str): Nodo de destino. 
                nueva_capacidad (float): Nueva capacidad para la arista entre el nodo de origen y el nodo de destino. 
            """ 
        if origen in self.grafo and destino in self.grafo[origen]: 
            self.grafo[origen][destino]['capacidad'] = nueva_capacidad

    def agregar_arista(self, origen, destino, capacidad, coste=1):
        """
        Agrega una arista al grafo con una capacidad dada.

        Argumentos:
            origen (int): Nodo de origen.
            destino (int): Nodo de destino.
            capacidad (float): Capacidad del enlace entre los nodos.
            coste (float): Coste del enlace entre los nodos.
        """
        if origen not in self.grafo:
            self.grafo[origen] = {}

        if destino not in self.grafo:
            self.grafo[destino] = {}

        self.grafo[origen][destino] = {'capacidad': capacidad, 'coste': coste}  
        self.num_vertices = len(self.grafo)
        
        self.num_aristas += 1

    def set_probabilidad_perdida(self, origen, destino, probabilidad):
        """
        Establece la probabilidad de pérdida para una arista específica en el grafo.
        Por defecto la probabilidad se establecerá en milisegundos. (Por ejemplo, se introduce 1 para 1 ms).
        
        Argumentos:
            origen (str): Nodo de origen.
            destino (str): Nodo de destino.
            probabilidad (float): Probabilidad de pérdida para la arista entre el nodo de origen y el nodo de destino.
        """
        if origen in self.grafo and destino in self.grafo[origen]:
            self.grafo[origen][destino]['prob_perdida'] = probabilidad
        else: 
            print(f"Error: No se encontró la arista entre {origen} y {destino} para establecer la probabilidad de pérdida.")
    
    def set_delay(self, origen, destino, delay):
        """
        Establece el delay para una arista específica en el grafo.
        Por defecto el delay se establecerá en milisegundos. (Por ejemplo, se introduce 1 para 1 ms).
        
        Argumentos:
            origen (str): Nodo de origen.
            destino (str): Nodo de destino.
            delay (float): Delay para la arista entre el nodo de origen y el nodo de destino.
        """
        if origen in self.grafo and destino in self.grafo[origen]:
            self.grafo[origen][destino]['delay'] = delay
        else: 
            print(f"Error: No se encontró la arista entre {origen} y {destino} para establecer el delay.")

    
    def cargar_desde_archivo(self, nombre_topologia):
        """
        Carga la matriz de capacidades y la matriz de tráfico.

        Argumentos:
            nombre_topologia (str): Nombre de la topología elegida. Proviene del menú inicial.
        """
        # Implementación para cargar la matriz de capacidades y la matriz de tráfico desde archivos

        ruta_capacidades = f"Topologias/Capacidades/{nombre_topologia}/{nombre_topologia}CapMatrix.csv"

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
                            self.agregar_arista(f"S{i + 1}", f"S{j + 1}", capacidad)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo de capacidades en la ruta: {ruta_capacidades}")
        pass
    
    def eliminar_arista(grafo, origen, destino):
        """
        Elimina una arista del grafo.

        Argumentos:
            grafo (Grafo): El grafo del cual se eliminará la arista.
            origen (node): Nodo de origen de la arista a eliminar.
            destino (node): Nodo de destino de la arista a eliminar.
        """
        if origen in grafo.grafo and destino in grafo.grafo[origen]:
            del grafo.grafo[origen][destino]

    def eliminar_nodo(grafo, nodo):
        """
        Elimina un nodo y todas sus aristas asociadas del grafo.

        Argumentos:
            grafo (Grafo): El grafo del cual se eliminará el nodo.
            nodo (node): Nodo a eliminar.
        """
        if nodo in grafo.grafo:
            del grafo.grafo[nodo]

        for origen in grafo.grafo:
            if nodo in grafo.grafo[origen]:
                del grafo.grafo[origen][nodo]
    
    def mostrar_diccionario(self):
        """
        Muestra el diccionario del grafo.
        """
        for origen, vecinos in self.grafo.items():
            print(f"{origen} -> {vecinos}")

    def mostrar_matriz_capacidades(self):
        """
        Muestra las capacidades restantes del grafo en formato de matriz 2D (Tabla).
        """
        # 1. Obtener todos los nodos únicos y ordenarlos alfabéticamente (A, B, C, D...)
        nodos = set(self.grafo.keys())
        for vecinos in self.grafo.values():
            nodos.update(vecinos.keys())
        nodos = sorted(list(nodos), key=lambda x: int(x[1:]))
        
        ancho = 8 # Ancho fijo para cada columna
        
        # 2. Imprimir el encabezado de las columnas
        encabezado = "    " + "".join([f"{nodo:>{ancho}}" for nodo in nodos])
        print(encabezado)
        
        # 3. Imprimir cada fila con su letra y sus valores
        for origen in nodos:
            fila_str = f"{origen:<3}" 
            for destino in nodos:
                capacidad = self.get_capacidad_arista(origen, destino)
                
                # Tu función get_capacidad_arista devuelve 'inf' si no hay enlace. 
                # Para la vista en matriz, es más bonito poner un 0.
                if capacidad == float('inf'):
                    capacidad = 0
                
                # Formatear el número para que ocupe 8 espacios y quede alineado
                fila_str += f"{capacidad:>{ancho}.1f}"
            print(fila_str)
        print("") # Salto de línea extra al final para que quede limpio


    def copiar_grafo(grafo):
        """
        Crea una copia del grafo dado.

        Argumentos:
            grafo (Grafo): El grafo a copiar.
        Returns:
            grafo_copia (Grafo): Una copia del grafo original.
        """

        grafo_copia = Grafo()
        for origen, vecinos in grafo.grafo.items():
            for destino, atributos in vecinos.items():
                grafo_copia.agregar_arista(origen, destino, atributos['capacidad'], atributos['coste'])

                if 'delay' in atributos:
                    grafo_copia.set_delay(origen, destino, atributos['delay'])

        return grafo_copia
    