class Trafico:
    def __init__(self):
        self.matriz_trafico = []  # Matriz de tráfico almacenada como un diccionario

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

                # Procesar las líneas para construir la matriz de tráfico
                for i, linea in enumerate(lineas):  # Procesar la fila
                    valores = linea.strip().split(',')

                    for j, valor in enumerate(valores):  # Procesar la columna
                        demanda = float(valor)
                        if demanda > 0:
                            if i not in self.matriz_trafico:
                                self.matriz_trafico[i] = {}
                            self.matriz_trafico[i][j] = demanda
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo de tráfico en la ruta: {ruta_trafico}")
        pass

    def mostrar_matriz_trafico(self):
        """
        Muestra la matriz de tráfico cargada en forma de tablas
        """
        print("\nMatriz de Tráfico Cargada:")
        for origen, destinos in self.matriz_trafico.items():
            for destino, demanda in destinos.items():
                print(f"De {origen} a {destino}: {demanda}")