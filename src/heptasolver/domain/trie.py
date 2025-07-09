import os
import json

from typing import List, Dict


RAE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'rae.json')
RAE_PATH = os.path.abspath(RAE_PATH)


class TrieNode:
    def __init__(self):
        self.words: List[str] = []
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_key: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, words: list):
        node = self.root
        for char in key.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_key = True
        node.words.extend(words)

    def search(self, key: str) -> bool:
        node = self.root
        for char in key.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_key
    
    def get_words_in_node(self, key: str) -> List[str]:
        node = self.root
        for char in key.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.words


class RAETrie(Trie):
    def __init__(self):
        super().__init__()
        with open(RAE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            for key, words in data.items():
                    self.insert(key, words)


