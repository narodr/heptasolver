from unidecode import unidecode
import os


RAE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'rae.txt')
RAE_PATH = os.path.abspath(RAE_PATH)


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