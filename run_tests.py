from src import menus as m

from Pruebas.shortestPath_test import (
    caso1_shortest_paths,
    caso2_shortest_paths,
    caso3_shortest_paths
)
from Pruebas.enrutamiento_test import (
    caso1_enrutamiento,caso2_enrutamiento, caso3_enrutamiento, caso4_enrutamiento, caso5_enrutamiento, 
    caso6_enrutamiento, caso7_enrutamiento, caso8_enrutamiento, caso9_enrutamiento, 
    caso_enrutamientoDelay, caso_enrutamiento_abilene_real)

from Pruebas.funciones_test import (
    test_calculo_retardo
)

if __name__ == "__main__":

    opcion = m.menu_pruebas()

    if opcion == 1:
        print("\nEjecutando pruebas de shortest path...\n")
        caso1_shortest_paths()
        caso2_shortest_paths()
        caso3_shortest_paths()
    elif opcion == 2:
        print("\nEjecutando prueba de enrutamiento...\n")
        print ("Ejecutando casos de enrutamiento con grafo1 y diferentes matrices de tráfico...\n")
        caso1_enrutamiento()
        caso2_enrutamiento() 
        caso3_enrutamiento() 
        caso4_enrutamiento() 
        caso5_enrutamiento() 
        print ("\nEjecutando caso de enrutamiento con grafo2 y diferentes matrices de tráfico...\n")
        caso6_enrutamiento()
        caso7_enrutamiento()
        caso8_enrutamiento()
        caso9_enrutamiento()
        print("\nEjecutando caso de enrutamiento con delays aleatorios...\n")
        caso_enrutamientoDelay()
        caso_enrutamiento_abilene_real()
    elif opcion == 3: 
        print("\nEjecutando prueba de cálculo de EPDD...\n")
        test_calculo_retardo()
    else:
        print("Saliendo del programa.")
