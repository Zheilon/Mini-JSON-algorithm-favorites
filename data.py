import json
from typing import Any
import keys

class JsonMethods:

    @staticmethod
    def readMyJson() -> dict:
        """
        Lee el archivo .json, para luego retornarlo como tipo dict
        """
        try:
            with open("favs.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                if not data:
                    data = {"favorites": []}

        except (FileNotFoundError, json.JSONDecodeError):
            data = {keys.FAVORITES: []}

        with open("favs.json", "w", encoding="utf-8") as file:
            JsonMethods.saveIn(data, file)

        return data


    @staticmethod
    def saveIn(data: dict, file):
        """
        Guarda el diccionario en un archivo .json
        """
        json.dump(data, file, indent=4, ensure_ascii=False)