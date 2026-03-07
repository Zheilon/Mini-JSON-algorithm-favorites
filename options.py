import json
import data as dt

def add_favorite():
    """ Añade un nuevo título favorito al json, favs.json """
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
    """ Elimina un favorito del json, favs.json """
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
    """ Actualiza un favorito del json, favs.json, la cual pide
    al usuario el nuevo título, nuevo url y nuevo comentario"""
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


def show_all_favorites():
    """ Imprime por consola, todos los títulos
    favoritos existentes dentro de favs.json """

    js = dt.JsonMethods.readMyJson()

    def printWith(string: str, idx: int):
        """ Función interna, se encarga de imprimir una linea
        después del favorito mostrado en el (for), añadiendo
        al final el indice de este título, mediante el formato
        utilizando en la variable, last_string.
        :param string: Se refiere al título, que aparece cuando se muestra la lista
        :param idx: Index del (for) donde se encuentra la función """

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