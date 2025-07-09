from itertools import combinations
from heptasolver.domain.heptagrama import Heptagrama
from heptasolver.domain.trie import RAETrie


class RAEGenerator:
    def __init__(self, heptagrama):
        self.heptagrama: Heptagrama = heptagrama
        self.dictionary: RAETrie = RAETrie()
        self._variations = None
        self._iterator = None

    def __iter__(self):
        if self._variations is None:
            self._variations = list(self.generate())
        self._iterator = iter(self._variations)
        return self

    def __next__(self):
        if self._iterator is None:
            self.__iter__()
        return next(self._iterator)

    def generate(self):
        keys = self._get_keys()
        for key in keys:
            words = self.dictionary.get_words_in_node(key)
            if not words:
                continue
            for word in words:
                yield word

    def _get_keys(self):
        letters = sorted(self.heptagrama.letras)
        keys = []
        for length in range(3, 8):
            for combo in combinations(letters, length):
                if self.heptagrama.centro in combo:
                    word = ''.join(combo)
                    keys.append(word)
        return keys