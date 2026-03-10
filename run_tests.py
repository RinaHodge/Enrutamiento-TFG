from src import menus as m

from Pruebas.shortestPath_test import (
    caso1_shortest_paths,
    caso2_shortest_paths,
    caso3_shortest_paths
)
from Pruebas.enrutamiento_test import (
    caso1_enrutamiento,caso2_enrutamiento, caso3_enrutamiento, caso4_enrutamiento, caso5_enrutamiento, caso6_enrutamiento)

if __name__ == "__main__":

    opcion = m.menu_pruebas()

    if opcion == 1:
        print("\nEjecutando pruebas de shortest path...\n")
        caso1_shortest_paths()
        caso2_shortest_paths()
        caso3_shortest_paths()
    elif opcion == 2:
        print("\nEjecutando prueba de enrutamiento...\n")
        caso1_enrutamiento()
        caso2_enrutamiento() 
        caso3_enrutamiento() 
        caso4_enrutamiento() 
        caso5_enrutamiento() 
        caso6_enrutamiento()
    elif opcion == 3: 
        print("\nEjecutando todas las pruebas...\n")
    else:
        print("Saliendo del programa.")
