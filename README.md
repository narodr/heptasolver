# heptasolver

Resuelve automáticamente un [heptagrama](https://elpais.com/juegos/heptagrama/)

> A partir de siete letras dispuestas de manera hexagonal, con una de ellas en la 
posición central, el objetivo es formar el máximo número de palabras de al menos tres letras.
Puedes repetir las letras, pero siempre debes incluir la que está en la posición central. 
No se admiten nombres propios, plurales ni formas verbales conjugadas (solo infinitivos). 

### Instalar

```sh
pip install .
```

### Usar

```sh
heptasolver --letras abdcefg --centro a
```

### Desarrollo

Instalar la librería en modo editable:

```sh
pip install -e .
```

y ejecutar los tests:

```sh
pytest
```
