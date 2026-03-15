import json
import os
import data as dt
from rich.console import Console
from rich.table import Table

def add_favorite():
    """
    Añade un nuevo título favorito al json, favs.json
    """
    os.system("cls")
    while True:
        js = dt.JsonMethods.readMyJson()
        title = str(input("Ingresa titulo: "))
        url = str(input("Ingresa URL: "))
        comment = str(input("Ingresa comentario: "))

        if not any(title == z['title'] for z in js['favorites']):
            js['favorites'].append({"title": title, "url": url, "comment": comment})
            with open("favs.json", "w", encoding="utf-8") as file:
                json.dump(js, file, indent=4, ensure_ascii=False)
            break
        else:
            print("¡El título de esta pelicula ya existe!\n")


def delete_favorite():
    """
    Elimina un favorito del json, favs.json
    """
    os.system("cls")
    deleted = True
    while deleted:
        js = dt.JsonMethods.readMyJson()
        print("¡Elige el titulo que deseas eliminar!")
        for z in range(len(js['favorites'])):
            print(f"[ {z + 1} ]. {js['favorites'][z]['title']}")
        title = str(input("¡Elige!: "))

        if any(title == z['title'] for z in js['favorites']):
            for z in range(len(js['favorites'])):

                if title == js['favorites'][z]['title']:
                    js['favorites'].pop(z)

                    with open("favs.json", "w", encoding="utf-8") as file:
                        json.dump(js, file, indent=4, ensure_ascii=False)

                    deleted = False
                    break


def update_favorite():
    """
    Actualiza un favorito del json, favs.json, la cual pide
    al usuario el nuevo título, nuevo url y nuevo comentario
    """
    os.system("cls")
    js = dt.JsonMethods.readMyJson()
    while True:
        print("Ingresa titulo del favorito a eliminar: ")
        for z in range(len(js['favorites'])):
            print(f"[ {z + 1} ]. {js['favorites'][z]['title']}")
        title = str(input("¡Elige!: "))

        if any(title == z['title'] for z in js['favorites']):
            new_title = str(input("Ingresa nuevo título: "))
            new_url = str(input("Ingresa nueva URL: "))
            new_comment = str(input("Ingresa nuevo comentario: "))

            for z in range(len(js['favorites'])):
                if title == js['favorites'][z]['title']:
                    js['favorites'][z] = {"title": new_title, "url": new_url, "comment": new_comment}

            with open("favs.json", "w", encoding="utf-8") as file:
                json.dump(js, file, indent=4, ensure_ascii=False)

            break

        else:
            print(f"¡No existe el título: {title}!\n")


def show_all_favorites_v1():
    """
    Imprime por consola, todos los títulos
    favoritos existentes dentro de favs.json
    """
    os.system("cls")
    js = dt.JsonMethods.readMyJson()

    def printWith(string: str, idx: int):
        """
        Función interna, se encarga de imprimir una linea
        después del favorito mostrado en el (for), añadiendo
        al final el indice de este título, mediante el formato
        utilizando en la variable, last_string.
        :param string: Se refiere al título, que aparece cuando se muestra la lista
        :param idx: Index del (for) donde se encuentra la función
        """

        last_string = f"> F [ {idx} ]\n"
        new_len = len(string) - len(last_string)

        for _ in range(new_len):
            print(end="-")

        print(end=last_string)

    init_message = f"* --------------+ Lista de favoritos [ {len(js['favorites'])} ] +-------------- *"
    print(init_message)

    for z in range(len(js['favorites'])):
        print(f"\nTítulo: {js['favorites'][z]['title']}\n"
              f"URL: {js['favorites'][z]['url']}\n"
              f"Comentario: {js['favorites'][z]['comment']}")
        printWith(init_message, idx=z + 1)


def show_all_fav_v2_rich():
    os.system("cls")
    data = dt.JsonMethods.readMyJson()
    console = Console(
        width=None,
        highlight=True,
        soft_wrap=True,
        emoji=True
    )

    table = Table(
        title="Favoritos",
        border_style="bright_blue",
        header_style="bold red",
        row_styles=["none", "dim"],
    )

    table.add_column("Títulos", style="cyan")
    table.add_column("URL", style="black")
    table.add_column("Comentario", style="black", overflow="fold")

    for z in data['favorites']:
        table.add_row(z['title'], z['url'], z['comment'])

    console.print(table)