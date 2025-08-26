from itertools import combinations
from heptasolver.domain.entities.heptagrama import Heptagrama
from heptasolver.domain.entities.trie import RAETrie


class Solver:
    def __init__(self, letras, centro):
        if isinstance(letras, str):
            # TODO: habria que unificar esto
            # 'abcdefg' -> ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            letras = list(letras)

        self.heptagrama: Heptagrama = Heptagrama(letras=letras, centro=centro)
        self.dictionary: RAETrie = RAETrie()
        self._variations = None
        self._iterator = None

    def is_playable(self):
        return len(self.solve_all()) != 0

    def solve_all(self):
        """Returns a list with all the words for the given game."""
        words = []
        keys = self._get_keys()
        for key in keys:
            if not self.dictionary.get_words_in_node(key):
                continue
            for word in self.dictionary.get_words_in_node(key):
                words.append(word)
        return words

    def solve_words_with_all_letters(self):
        """Returns a list with the words containing all 7 letters."""
        key = ''.join(sorted(set(self.heptagrama.letras)))
        return self.dictionary.get_words_in_node(key)

    def solve_by_initial_letter(self, letter: str):
        """Returns a list with all the words beginning with the letter"""
        words = []
        keys = self._get_keys(contains_letter=letter)
        for key in keys:
            if not self.dictionary.get_words_in_node(key):
                continue
            for word in self.dictionary.get_words_in_node(key):
                if word[0] == letter:
                    words.append(word)
        return words

    def _get_keys(self, contains_letter=None):
        letters = sorted(self.heptagrama.letras)

        if contains_letter and contains_letter not in letters:
            raise Exception

        keys = []
        for length in range(3, 8):
            for combo in combinations(letters, length):
                if ((self.heptagrama.centro in combo) 
                    and (contains_letter in combo if contains_letter else True)):
                    word = ''.join(combo)
                    keys.append(word)
        return keys
