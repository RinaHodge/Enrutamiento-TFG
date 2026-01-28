class Grafo:
    def __init__(self):
        self.grafo = {}         # Diccionario para almacenar los vértices y sus aristas
        self.num_vertices = 0

    def agregar_arista(self, origen, destino, coste):
        """
        Agrega una arista al grafo con una capacidad dada.

        Argumentos:
            origen (int): Nodo de origen.
            destino (int): Nodo de destino.
            capacidad (float): Capacidad del enlace entre los nodos.
        """
        if origen not in self.grafo:
            self.grafo[origen] = {}

        if destino not in self.grafo:
            self.grafo[destino] = {}

        self.grafo[origen][destino] = coste
        self.num_vertices = len(self.grafo)


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
                        coste = float(valor)

                        #Si la capacidad es mayor que 0, agregar la arista al grafo. Si es menor, no hay enlace
                        if coste > 0:
                            self.agregar_arista(self.mapeo_letra(i), self.mapeo_letra(j), coste)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo de capacidades en la ruta: {ruta_capacidades}")
        pass
    
    def mapeo_letra(self, indice):
        """
        Mapea un índice numérico a una letra correspondiente (0 -> A, 1 -> B, etc.).

        Argumentos:
            indice (int): Índice numérico a mapear.

        Returns:
            str: Letra correspondiente al índice.
        """
        return chr(ord('A') + indice)
    
    def mostrar_diccionario(self):
        """
        Muestra el diccionario del grafo.
        """
        for origen, vecinos in self.grafo.items():
            print(f"{origen} -> {vecinos}")