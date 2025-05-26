import pyautogui
import time


FILE_NAME = "candidatos.txt"
INIT_DELAY = 5
TIME_BETWEEN_WORDS = .01


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\rEmpezando en {i}...", end="", flush=True)
        time.sleep(1)


def palabras_generator():
    with open(FILE_NAME, "r") as file:
        for line in file:
            yield line.strip()


if __name__ == "__main__":
    countdown(INIT_DELAY)
    for palabra in palabras_generator():
        pyautogui.write(palabra)
        pyautogui.press("enter")
        time.sleep(TIME_BETWEEN_WORDS)
    print("Todas las palabras han sido escritas.")

