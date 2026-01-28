class Trafico:
    def __init__(self):
        self.matriz_trafico = []  # Matriz de tráfico (lista de listas)

    def cargar_matriz_trafico(self, nombre_topologia, id_trafico):
        """
        Carga la matriz de tráfico desde un archivo CSV.

        Argumentos:
            nombre_topologia (str): Nombre de la topología elegida.
            id_trafico (str): Identificador del archivo de tráfico (TM1-TM5).
        """
        ruta_trafico = f"Topologias/Matrices_Trafico/{nombre_topologia}/{nombre_topologia}{id_trafico}.csv"

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

    def mostrar_matriz_trafico(self):
        """
        Muestra la matriz de tráfico cargada en forma de tablas
        """
        print("\nMatriz de Tráfico Cargada:")
        for fila in self.matriz_trafico:
            print(fila)