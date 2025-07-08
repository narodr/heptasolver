import pytest
from unittest.mock import patch
from heptasolver.domain.generador import RAEGenerator
from heptasolver.domain import generador

class DummyHeptagrama:
    def __init__(self, letras, centro):
        self.letras = letras
        self.centro = centro

@pytest.fixture
def dummy_heptagrama():
    # letras must be 7 unique letters, centro must be one of them
    return DummyHeptagrama(letras="abcdefg", centro="c")

@pytest.fixture
def mock_raetrie(monkeypatch):
    # Patch RAETrie so it doesn't read the file and can be controlled
    class DummyTrie:
        def __init__(self):
            self.words = set()
        def insert(self, word):
            self.words.add(word)
        def search(self, word):
            return word in self.words
    monkeypatch.setattr(generador, "RAETrie", DummyTrie)
    return DummyTrie

def test_generate_yields_valid_words(dummy_heptagrama):
    # Patch RAETrie to only accept a few words
    valid_words = {"cab", "face", "bed", "fed", "cafe"}
    with patch("src.generador.RAETrie") as MockTrie:
        trie_instance = MockTrie.return_value
        trie_instance.search.side_effect = lambda w: w in valid_words

        gen = RAEGenerator(dummy_heptagrama)
        words = set(gen.generate())
        # Only words containing centro 'c' and in valid_words should be yielded
        expected = {w for w in valid_words if "c" in w and set(w).issubset(set("abcdefg"))}
        assert words == expected

def test_iter_and_next(dummy_heptagrama):
    valid_words = {"cab", "cafe"}
    with patch("src.generador.RAETrie") as MockTrie:
        trie_instance = MockTrie.return_value
        trie_instance.search.side_effect = lambda w: w in valid_words

        gen = RAEGenerator(dummy_heptagrama)
        it = iter(gen)
        results = set()
        try:
            while True:
                results.add(next(it))
        except StopIteration:
            pass
        expected = {w for w in valid_words if "c" in w and set(w).issubset(set("abcdefg"))}
        assert results == expected

def test_generate_no_valid_words(dummy_heptagrama):
    with patch("src.generador.RAETrie") as MockTrie:
        trie_instance = MockTrie.return_value
        trie_instance.search.return_value = False

        gen = RAEGenerator(dummy_heptagrama)
        words = list(gen.generate())
        assert words == []

def test_is_in_rae_calls_dictionary(dummy_heptagrama):
    with patch("src.generador.RAETrie") as MockTrie:
        trie_instance = MockTrie.return_value
        trie_instance.search.return_value = True

        gen = RAEGenerator(dummy_heptagrama)
        assert gen._is_in_rae("cafe")
        trie_instance.search.assert_called_with("cafe")