import options as opt
import show_menu as sm

def main():
    """
    Función principal que desarrolla el programa. Se recomienda usar
    este algoritmo por consola de [ powershell o cmd ], para poder
    aprovechar las funciones de la libreria rich, que permite mostrar
    una tabla mucho más elegante y personalizada.
    """
    while True:
        option = sm.genMenu()

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