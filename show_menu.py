import os
TITLE = "+-------------> Tus Favoritos <-------------+"

def genMenu() -> int:
    """
    Se encarga de mostrar el menú de selección en forma de tabla
    """

    n = len(TITLE) - 1
    options = ["Añadir", "Eliminar", "Modificar", "Ver lista", "Salir"]
    # Por cada opción, al inicio añado |, al final, y aquí debe ir space bro! |
    # En las esquinas debe ir un (+).
    # las opciones se mostraran de esta manera | [ 1. ] Añadir               |

    # Mando título.
    print("*".ljust(n, "-") + "*")
    print(TITLE)
    print("*".ljust(n, "-") + "*")
    # Luego el subtítulo Opciones.
    # --------------------------
    # | Opciones               |
    # -------------------------
    # Debo hacer 2 iteracciones.
    for z in range(2):
        if z == 1:
            # Ojoooo! este espacio antes del palo, es vital!!|
            text_ = f"| Opciones...!"
            # Esto es multiplicación de Strings en Python!!!!
            print(text_.ljust(n) + "|")
        print("+".ljust(n, "-") + "+")
    # este parte termina así: +-----------------------+

    # Ahora le doy formato al menú de opciones.
    for z in range(len(options)):
        text = f"| [ {z + 1} ]. {options[z]}"
        print(text.ljust(n) + "|")
        print("+".ljust(n, "-") + "+")

    # Este se pone por acá como para que
    # halla un margen para escribir.
    print()
    return int(input("Ingresa tu opción: "))