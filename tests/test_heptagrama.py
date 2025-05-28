import pytest
from pydantic import ValidationError
from src.heptagrama import Heptagrama


def test_valid_heptagrama():
    h = Heptagrama(letras=["a", "b", "c", "d", "e", "f", "g"], centro="a")
    assert h.letras == ["a", "b", "c", "d", "e", "f", "g"]
    assert h.centro == "a"


def test_letras_too_few():
    with pytest.raises(ValidationError) as exc:
        Heptagrama(letras=["a", "b", "c", "d", "e", "f"], centro="a")
    assert "must contain exactly 7 characters" in str(exc.value)


def test_letras_too_many():
    with pytest.raises(ValidationError) as exc:
        Heptagrama(letras=["a", "b", "c", "d", "e", "f", "g", "h"], centro="a")
    assert "must contain exactly 7 characters" in str(exc.value)


def test_letras_duplicates():
    with pytest.raises(ValidationError) as exc:
        Heptagrama(letras=["a", "b", "c", "d", "e", "f", "a"], centro="a")
    assert "characters in the list must be unique" in str(exc.value)


def test_letras_non_single_char():
    with pytest.raises(ValidationError) as exc:
        Heptagrama(letras=["ab", "b", "c", "d", "e", "f", "g"], centro="a")
    assert "Each item in the list must be a single character" in str(exc.value)


def test_centro_not_in_letras():
    with pytest.raises(ValidationError) as exc:
        Heptagrama(letras=["a", "b", "c", "d", "e", "f", "g"], centro="z")
    assert "must be one of the characters" in str(exc.value)


def test_centro_not_single_char():
    with pytest.raises(ValidationError) as exc:
        Heptagrama(letras=["a", "b", "c", "d", "e", "f", "g"], centro="ab")
    # El mensaje puede ser por 'no está en letras' o por longitud, así que acepta cualquiera
    assert (
        "must be a single character" in str(exc.value) 
        or "must be one of the characters" in str(exc.value)
    )

