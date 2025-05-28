from typing import List
from pydantic import BaseModel, field_validator


FILE_NAME = "candidatos.txt"
INIT_DELAY = 5
TIME_BETWEEN_WORDS = .01


class Heptagrama(BaseModel):
    letras: List[str]
    centro: str

    @field_validator('letras')
    def validar_letras(self):
        if len(self.letras) != 7:
            raise ValueError('The list must contain exactly 7 characters.')
        if len(set(self.letras)) != 7:
            raise ValueError('The characters in the list must be unique.')
        for char in self.letras:
            if len(char) != 1:
                raise ValueError('Each item in the list must be a single character.')
        return self

    @field_validator('centro')
    def validar_centro(self):
        if self.centro not in self.letras:
            raise ValueError('The special character must be one of the characters '
                             'in the list.')
        if len(self.centro) != 1:
            raise ValueError('The special character must be a single character.')
        return self


