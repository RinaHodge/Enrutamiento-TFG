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
        print("1. Abeline")
        print("2. Geant")
        print("3. Germany")
        print("4. Nobel")
        print("Q. Salir")

        opcion = input("Seleccione la topología a enrutar:")

        if opcion == '1':
            nombre = "Abeline"
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

        trafico_opcion = input("Seleccione el tipo de tráfico: ")

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
