import random
import src.utils as utils


MAX_PALABRAS = 200
MIN_STR_LENGTH = 3
MAX_STR_LENGTH = 7
FILE_NAME = "candidatos.txt"


letras = ["s", "a", "e", "c", "r", "l", "f"]
centro = "f" 


def generar_palabras(letras, centro):
    palabras = []
    while len(palabras) < MAX_PALABRAS:
        palabra = ""
        while True:
            longitud = random.randint(MIN_STR_LENGTH, MAX_STR_LENGTH)
            palabra = "".join(random.choices(letras, k=longitud))
            if centro in palabra and palabra not in palabras:
                palabras.append(palabra)
                break
    return palabras


if __name__ == "__main__":
    palabras = generar_palabras(letras, centro)
    utils.escribir_palabras(palabras, FILE_NAME)
    print(f"{len(palabras)} palabras y se han guardado en '{FILE_NAME}'")
