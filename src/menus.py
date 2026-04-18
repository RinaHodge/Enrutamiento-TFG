def menu_inicial() -> tuple:
    """
    Muestra el menú interactivo para seleccionar la topología y el tráfico.

    Solicita al usuario que elija una red (Abilene, Geant, etc.) y un nivel
    de carga de tráfico (TM1-TM5). Valida las entradas para evitar errores.

    Returns:
        tuple: Una tupla con dos valores (nombre_topologia, id_trafico).
               Ejemplo: ("Abilene", "TM1").
               Devuelve (None, None) si el usuario elige salir.
    """

    nombre = ''                     #es el nombre del archivo de la topología
    trafico = ''                    #es el nombre del archivo de tráfico

    while True:
        print("\n--- MENÚ DE ENRUTAMIENTO ---")
        print("1. Abilene")
        print("2. Geant")
        print("3. Germany")
        print("4. Nobel")
        print("Q. Salir")

        opcion = input("Seleccione la topología a enrutar:")

        if opcion == '1':
            nombre = "Abilene"
        elif opcion == '2':
            nombre = "Geant"
        elif opcion == '3':
            nombre = "Germany"
        elif opcion == '4':
            nombre = "Nobel"
        elif opcion == 'Q' or opcion == 'q':
            print("Saliendo del menú.")
            return None, None
        else:
            print("Opción no válida. Por favor, intente de nuevo.\n")
            continue

        print("\nHa seleccionado la topología:", nombre)

        print("\n--- Selección de tráfico ---")
        print("1. TM1")
        print("2. TM2")
        print("3. TM3")
        print("4. TM4")
        print("5. TM5")

        trafico_opcion = input("Seleccione el tipo de tráfico: ").strip()

        if not trafico_opcion.isdigit():
             print("Error: Debe introducir un número.\n")
             continue
        
        if int(trafico_opcion) > 6 or int(trafico_opcion) < 1:
            print("Opción no válida. Por favor, intente de nuevo.\n")
            continue
        
        else:
            print("\nHa seleccionado el tráfico:", "TM" + trafico_opcion)
            trafico = "TM" + trafico_opcion
            break
        
    return nombre, trafico

def menu_pruebas() -> int:
    """
    Muestra el menú interactivo para seleccionar la prueba a ejecutar. Solicita al usuario que elija una prueba"
    returns: 
    int: El número de la prueba seleccionada por el usuario. Devuelve -1 si el usuario elige salir.
    """

    while True: 
        print("\n--- MENÚ DE PRUEBAS ---")
        print("1. Prueba de los k mejores caminos (Shortest Path)")
        print("2. Prueba de enrutamiento")
        print("Q. Salir")

        opcion = input("Seleccione la prueba a ejecutar: ").strip()

        if opcion == "Q" or opcion == "q":
            opcion = 0
            print ("Saliendo del menú.") 
            return 0
        
        if not opcion.isdigit():
            print("Error: Debe introducir un número.\n") 
            continue

        opcion = int(opcion)
        if opcion > 2 or opcion < 0:
            print("Opción no válida. Por favor, intente de nuevo.\n") 
            continue 
        
        else:
            return opcion
        
def menu_epdd() -> int: 
    """
    Muestra el menú interactivo para seleccionar el EPDD a ejecutar. Solicita al usuario que elija un EPDD aleatorio o específico para ejecutar. Valida las entradas para evitar errores."
    returns: 
    int: El número del EPDD seleccionado por el usuario. Devuelve -1 si el usuario elige salir.
    """

    while True: 
        print("\n--- Cálculo de EPDD ---")
        print("1. EPDD aleatorio")
        print("2. EPDD por ruta")
        print("Q. Salir")

        opcion = input("Seleccione el EPDD a ejecutar: ").strip()

        if opcion == "Q" or opcion == "q":
            opcion = 0
            print ("Saliendo del menú.") 
            return 0
        
        if not opcion.isdigit():
            print("Error: Debe introducir un número.\n") 
            continue

        opcion = int(opcion)
        if opcion > 2 or opcion < 0:
            print("Opción no válida. Por favor, intente de nuevo.\n") 
            continue 
        
        else:
            return opcion
        
def menu_eleccion_ruta(nodos_disponibles) -> tuple:
    """
    Muestra el menú interactivo para seleccionar un nodo TA de la ruta a explorar. Solicita al usuario que elija un nodo TA de la ruta a explorar. Valida las entradas para evitar errores."
    returns: 
    tuple: Los nodos origen y destino seleccionados por el usuario. Devuelve None si el usuario elige salir.
    """
    print("\n--- NODOS DISPONIBLES EN LA RED ---")
    for i, nodo in enumerate(nodos_disponibles):
        print(f"[{i+1}] Nodo '{nodo}'")
    print("-----------------------------------")

    while True:
        origen = int(input("\nIngrese el NÚMERO del nodo origen: ")) - 1
        destino = int(input("Ingrese el NÚMERO del nodo destino: ")) - 1

        # Validar que las entradas sean números enteros y estén dentro del rango de nodos disponibles
        if not (0 <= origen < len(nodos_disponibles)) or not (0 <= destino < len(nodos_disponibles)):
            print("Error: Número de nodo inválido. Por favor, intente de nuevo.")
            continue
        else:
            return nodos_disponibles[origen], nodos_disponibles[destino]

def menu_proba_perdida() -> int:
    """
    Muestra el menú interactivo para seleccionar la probabilidad de pérdida a establecer en las aristas del grafo. Solicita al usuario que elija una probabilidad de pérdida para establecer en las aristas del grafo. Valida las entradas para evitar errores."
    returns: 
    int: La probabilidad de pérdida seleccionada por el usuario. Devuelve None si el usuario elige salir.
    """

    while True: 
        print("\n--- PROBABILIDAD DE PÉRDIDA ---")
        print("1. Por defecto ")
        print("2. Random")

        opcion = input("Seleccione la probabilidad de pérdida a establecer en las aristas del grafo: ").strip()
        
        if not opcion.isdigit():
            print("Error: Debe introducir un número.\n") 
            continue

        opcion = int(opcion)
        if opcion > 2 or opcion < 0:
            print("Opción no válida. Por favor, intente de nuevo.\n") 
            continue 
        else: 
            break
        
    return opcion