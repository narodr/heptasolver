from typing import List
from pydantic import BaseModel, ValidationInfo, field_validator


# TODO: Implementar tipos Annotated con StringConstraints para los atributos
class Heptagrama(BaseModel):
    letras: List[str]
    centro: str

    @field_validator('letras')
    @classmethod
    def validar_letras(cls, values: List[str]) -> List[str]:
        if len(values) != 7:
            raise ValueError('The list must contain exactly 7 characters.')
        if len(set(values)) != 7:
            raise ValueError('The characters in the list must be unique.')
        for char in values:
            if len(char) != 1:
                raise ValueError('Each item in the list must be a single character.')
        return values

    @field_validator('centro')
    @classmethod
    def validar_centro(cls, values: str, info: ValidationInfo) -> str:
        letras = info.data.get('letras')
        if letras is not None and values not in letras:
            raise ValueError('The special character must be one of the characters in the list.')
        return values



