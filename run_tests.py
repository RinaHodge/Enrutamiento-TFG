import Menus as m

from Pruebas.ShortestPathTest import (
    caso1_shortest_paths,
    caso2_shortest_paths,
    caso3_shortest_paths
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
        caso2_shortest_paths()
    elif opcion == 3: 
        
        caso3_shortest_paths()
    else:
        print("Saliendo del programa.")
