from itertools import permutations, combinations
from src.heptagrama import Heptagrama
from unidecode import unidecode


RAE_PATH = '../data/rae.txt'


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word) -> bool:
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


class RAETrie(Trie):
    def __init__(self):
        super().__init__()
        with open(RAE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                if word:
                    word = unidecode(word)
                    self.insert(word)


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




