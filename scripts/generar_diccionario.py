"""
Genera un diccionario a partir de un listado de palabras.

El diccionario es del tipo Dict[str, List] donde las palabras de cada lista están
agrupadas según la llave, que es una cadena con sus letras únicas ordenadas alfabéticamente.

E. g.:

{
  "ab": [
    "aba",
    "abaa",
    "baba"
  ]
}
"""

import json
import os
from unidecode import unidecode
from collections import defaultdict


INPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'rae.txt')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'rae.json')


def write_json_file(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_key(word: str):
    key = ''.join(sorted(set(word)))
    return key


def main():
    hashmap = defaultdict(list)
    with open(INPUT_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            word = unidecode(line.strip())
            key = get_key(word)
            hashmap[key].append(word)
    write_json_file(hashmap, OUTPUT_PATH)


if __name__ == "__main__":
    main()