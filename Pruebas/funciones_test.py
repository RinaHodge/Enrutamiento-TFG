from src.funciones import *

def test_calculo_retardo():
    # ===============================
    # CASO 1: Prueba controlada 
    # ===============================

    # Crear el grafo
    g = Grafo()

    g.agregar_arista("S1", "S2", 10)
    g.agregar_arista("S2", "S1", 10)

    g.agregar_arista("S2", "S3", 30)
    g.agregar_arista("S3", "S2", 30)

    g.set_probabilidad_perdida("S1", "S2", 0.1)
    g.set_probabilidad_perdida("S2", "S1", 0.1)
    g.set_probabilidad_perdida("S2", "S3", 0.1)
    g.set_probabilidad_perdida("S3", "S2", 0.1)

    g.set_delay("S1", "S2", 1)
    g.set_delay("S2", "S1", 1)
    g.set_delay("S2", "S3", 1)
    g.set_delay("S3", "S2", 1)

    ruta1 = ["S1", "S2", "S3"]

    #Los EPDD esperados son (python agrega decimales por el formato de impresión)
    #EPDD en S1: 2.5434
    #EPDD en S2: 2.494
    #EPDD en S3: 

    nodo_TA1, epdd_optimo1 = calculo_EPDD_optimo(g, ruta1, n = 2, m = 2)
    print(f"El nodo TA calculado para el grafo 1 es: {nodo_TA1} con un EPDD de: {epdd_optimo1}")
    
    # ===============================
    # CASO 2: Prueba controlada, 0% de pérdidas (probabilidad de pérdida = 0). 
    # ===============================
    
    # ===============================
    # CASO 3: Prueba controlada, asimetría
    # ===============================
    # Crear el grafo
    g3 = Grafo()

    g3.agregar_arista("S1", "S2", 100)
    g3.agregar_arista("S2", "S1", 100)
    g3.agregar_arista("S2", "S3", 100)
    g3.agregar_arista("S3", "S2", 100)

    g3.set_probabilidad_perdida("S1", "S2", 0.1)
    g3.set_probabilidad_perdida("S2", "S1", 0.1)
    g3.set_probabilidad_perdida("S2", "S3", 0.1)
    g3.set_probabilidad_perdida("S3", "S2", 0.1)

    # Retardos asimétricos
    g3.set_delay("S1", "S2", 2)  
    g3.set_delay("S2", "S1", 50)  
    g3.set_delay("S2", "S3", 2)   
    g3.set_delay("S3", "S2", 50)  

    ruta3 = ["S1", "S2", "S3"]
    #Los EPDD esperados son (python agrega decimales por el formato de impresión)
    #EPDD en S1:
    #EPDD en S2: 
    #EPDD en S3: 

    nodo_TA3, epdd_optimo3 = calculo_EPDD_optimo(g3, ruta3, n = 2, m = 2)
    print(f"El nodo TA calculado para el grafo 3 es: {nodo_TA3} con un EPDD de: {epdd_optimo3}")