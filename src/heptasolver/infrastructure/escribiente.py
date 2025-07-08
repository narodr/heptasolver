import pyautogui
import time
import heptasolver.utils as utils
from typing import Union


INIT_DELAY = 5          # segundos de espera iniciales
TIME_BETWEEN = .01      # segundos entre cada llamada


class Escribiente:
    def __init__(self, 
                 init_delay=INIT_DELAY, 
                 time_between_words=TIME_BETWEEN):
        self.init_delay = init_delay
        self.time_between_words = time_between_words
        self._has_counted_down = False

    def escribir(self, contenido: Union[str, list]):
        if not self._has_counted_down:
            utils.countdown(self.init_delay)
            self._has_counted_down = True
        if isinstance(contenido, str):
            palabras = [contenido]
        else:
            palabras = list(contenido)
        for palabra in palabras:
            pyautogui.write(str(palabra))
            pyautogui.press("enter")
            time.sleep(self.time_between_words)
