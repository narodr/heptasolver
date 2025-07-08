from itertools import permutations
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
        seen = set()
        for length in range(3, 8):
            for p in permutations(self.heptagrama.letras, length):
                if self.heptagrama.centro in p:
                    word = ''.join(p)
                    if word not in seen and self._is_in_rae(word):
                        seen.add(word)
                        yield word

    def _is_in_rae(self, word: str) -> bool:
        return self.dictionary.search(word)




