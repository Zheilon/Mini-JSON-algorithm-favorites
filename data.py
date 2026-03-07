import json
from typing import Any

class JsonMethods:

    @staticmethod
    def readMyJson() -> dict:
        """ Lee el archivo .json, para luego retornarlo como tipo dict """
        try:
            with open("favs.json", "r", encoding="utf-8") as file:
                js = json.load(file)

                if not js:
                    js = {"favorites": []}

        except (FileNotFoundError, json.JSONDecodeError):
            js = {"favorites": []}

        with open("favs.json", "w", encoding="utf-8") as file:
            json.dump(js, file, indent=4, ensure_ascii=False)

        return js


    def insert(self, key: str, value: Any):
        """ Inserta un nuevo atributo en el archivo json. Realiza una validación
        para determinar que la key entrante no exista en el .json
         :param key: Nombre del atributo
         :param value: Contenido del atributo """
        data = self.readMyJson()

        if key in data:
            print("¡Esta clave ya existe!")
            return

        data[key] = value
        with open("favs.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def deleteAttribute(self, key):
        """ Elimina un atributo del archivo json. Esta función valida
        si la key del parametro existe.
         :param key: Nombre del atributo """
        data = self.readMyJson()

        if key not in data:
            print(f"¡Tu key [{key}] no existe!")
            return

        del data[key]
        with open("favs.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def updateAttribute(self, key, value):
        """ Actualiza el valor de un atributo especificado por parametro, en
        el archivo .json
         :param key: Nombre del atributo
         :param value: Valor para asignare a la key """
        data = self.readMyJson()

        if key not in data:
            print(f"¡Tu key [{key}] no existe!")
            return

        data[key] = value
        with open("favs.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)