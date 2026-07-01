# Enrutamiento y Posicionamiento Óptimo del Transport Assistant (TA) mediante Machine Learning

Este repositorio/carpeta contiene el código fuente desarrollado para el Trabajo de Fin de Grado (TFG). El objetivo principal del software es simular entornos de redes, calcular el Expected Packet Delivery Delay (EPDD) bajo condiciones de pérdida y retardo, y generar conjuntos de datos (datasets) para entrenar modelos de Machine Learning que predigan el nodo óptimo donde posicionar la función de red TA (Transport Assistant).

## 📁 Estructura del Proyecto

El código está organizado de forma y con el paradigma de la Programación Orientada a Objetos

* **`src/`**: Contiene el núcleo lógico del simulador.
    * `clase_grafo.py`: Gestión de la topología de red (nodos, aristas, retardos, pérdidas).
    * `clase_trafico.py`: Gestión de las matrices de tráfico y demandas.
    * `funciones.py`: Algoritmos matemáticos (Dijkstra, Yen's K-Shortest Paths, cálculo de EPDD y EPDD óptimo).
    * `menus.py`: Interfaz de terminal para la ejecución interactiva.
* **`Topologias/`**: Datos estáticos de las redes de estudio (Abilene, Geant, Germany, Nobel), divididos en matrices de capacidad y de tráfico.
* **`Pruebas/`**: Casos de prueba controlados para validar el correcto funcionamiento de los algoritmos (rutas más cortas, cálculos de retardo, etc.).
* **`Dataset/`**: Directorio donde se almacenan los archivos `.csv` generados por las simulaciones para su posterior uso en Machine Learning.
* **Scripts en la raíz**: Archivos ejecutables principales para interactuar con el proyecto (ver sección de "Instrucciones de Uso").

## 📄 Archivos explicados
* **`actualizar_csv.py`**: Se utilizó para la cambiar la representación de los nodos en el `.csv`, en el cual estaban representados con letras. 
* **`balancear_clases.py`**: Este script se utilizó para generar más datos de la clase S5, en el tercer entrenamiento. 
* **`Consola.txt`**: Se escribió este archivo para controlar la generación de datos del primer script realizado.
* **`Consola_v2.txt`**: En este archivo se controlaba la generación de datos para un segundo script.

## ⚙️ Requisitos del Sistema

Para ejecutar el código correctamente, se requiere:
* Python 3.8 o superior.
* Librerías estándar de Python (`csv`, `os`, `random`, `heapq`, `unittest`).

## 🚀 Instrucciones de Uso

### 1. Ejecución del simulador interactivo
Para iniciar el programa principal que permite seleccionar topologías y realizar enrutamientos manuales, ejecuta:
```bash
python main.py
```
### 1. Ejecución del simulador interactivo
Para ejecutar las pruebas del programa se ejecuta: 
```bash
python run_tests.py
```

