import options as opt

def main():
    """
    Función principal que desarrolla el programa. Se recomienda usar
    este algoritmo por consola de [ powershell o cmd ], para poder
    aprovechar las funciones de la libreria rich, que permite mostrar
    una tabla mucho más elegante y personalizada.
    """
    while True:
        print("\n--------- Tus Favoritos ---------\n")

        options = ["Añadir", "Eliminar", "Modificar", "Ver lista", "Salir\n"]
        print(" * Opciones * ")

        for z in range(len(options)):
            print(f"[ {z + 1} ]. {options[z]}")
        option = int(input("¡Elige!: "))

        if option == 1:
            opt.add_favorite()

        if option == 2:
            opt.delete_favorite()

        if option == 3:
            opt.update_favorite()

        if option == 4:
            opt.show_all_fav_v2_rich()

        if option == 5:
            break

if __name__ == '__main__':
    main()