import time


def countdown(segundos):
    for i in range(segundos, 0, -1):
        print(f"\rEmpezando en {i}...", end="", flush=True)
        time.sleep(1)