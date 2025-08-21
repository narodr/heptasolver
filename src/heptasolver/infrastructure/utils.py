import time
import random


ABECEDARY = list('abcdefghijklmnopqrstuvwxyz')
VOWELS = 'aeiou'


def countdown(segundos):
    for i in range(segundos, 0, -1):
        print(f"\rEmpezando en {i}", end="", flush=True)
        time.sleep(1)
    print(f"\rEscribiendo...", flush=True)


def get_random_letters(center: str) -> str:
    center = center.lower()
    if len(center) != 1 or center not in ABECEDARY:
        raise ValueError("Center must be a single alphabetic character.")

    abc = ABECEDARY.copy()
    abc.remove(center)
    available_vowels = [v for v in VOWELS if v != center]
    selected_vowels = random.sample(available_vowels, 2)
    available_pool = list(set(abc) - set(selected_vowels))
    selected_rest = random.sample(available_pool, 4)
    # Remaining letters to choose: 7 - 2 vowels - 1 center = 4

    result = selected_vowels + selected_rest + [center]
    random.shuffle(result)

    return ''.join(result)


def get_random_center(letters: str=None) -> str:
    if not letters:
        letters = ABECEDARY.copy()
    index = random.randrange(len(letters))
    return letters[index]