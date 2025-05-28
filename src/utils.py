import time


def escribir_palabras(palabras, file_name):
    with open(file_name, "w") as file:
        for palabra in palabras:
            file.write(palabra + "\n")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\rEmpezando en {i}...", end="", flush=True)
        time.sleep(1)