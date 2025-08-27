import pytest
from unittest.mock import MagicMock
from heptasolver.domain.services.solver import Solver


@pytest.fixture
def mock_heptagrama():
    mock = MagicMock()
    mock.letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    mock.centro = 'e'
    return mock

@pytest.fixture
def mock_dictionary():
    mock = MagicMock()
    mock.get_words_in_node.side_effect = lambda key: {
        'abc': ['abc'],
        'abcdefg': ['abcdefg'],
        'cde': ['cde'],
        'bce': ['bce'],
        'befg': ['febeg', 'befg']
    }.get(key, [])
    return mock

@pytest.fixture
def solver(monkeypatch, mock_heptagrama, mock_dictionary):
    s = Solver(letras=mock_heptagrama.letras, centro=mock_heptagrama.centro)
    monkeypatch.setattr(s, 'heptagrama', mock_heptagrama)
    monkeypatch.setattr(s, 'dictionary', mock_dictionary)
    return s

def test_is_playable(solver):
    assert solver.is_playable() is True
def test_solve_all(solver):
    words = solver.solve_all()
    assert 'abc' in words or 'abcdefg' in words or 'cde' in words

def test_solve_words_with_all_letters(solver):
    words = solver.solve_words_with_all_letters()
    assert words == ['abcdefg']

def test_solve_by_initial_letter(solver):
    words = solver.solve_by_initial_letter('b')
    assert 'bce' in words
    assert 'befg' in words
    assert all(word.startswith('b') for word in words)

def test_get_keys_contains_letter(solver):
    keys = solver._get_keys(contains_letter='e')
    assert all('e' in key for key in keys)

def test_get_keys_invalid_letter(solver):
    with pytest.raises(Exception):
        solver._get_keys(contains_letter='z')

