import pyautogui
import time
import src.utils as utils


FILE_NAME = "candidatos.txt"
INIT_DELAY = 5
TIME_BETWEEN_WORDS = .01


def palabras_generator():
    with open(FILE_NAME, "r") as file:
        for line in file:
            yield line.strip()


if __name__ == "__main__":
    utils.countdown(INIT_DELAY)
    for palabra in palabras_generator():
        pyautogui.write(palabra)
        pyautogui.press("enter")
        time.sleep(TIME_BETWEEN_WORDS)
    print("Todas las palabras han sido escritas.")