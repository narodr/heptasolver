# heptasolver

Juega o resuelve un [heptagrama](https://elpais.com/juegos/heptagrama/)

> A partir de siete letras dispuestas de manera hexagonal, con una de ellas en la 
posición central, el objetivo es formar el máximo número de palabras de al menos 
tres letras.
Puedes repetir las letras, pero siempre debes incluir la que está en la posición central. 
No se admiten nombres propios, plurales ni formas verbales conjugadas (solo infinitivos). 

### Jugar una partida

Puedes jugar una partida a través de la terminal ejecutando el comando play. Opcionalmente puedes especificar el centro o las letras que quieres jugar.

```sh
heptasolver play [-l abcdefg] [-c a]
```

## Instalación

Clona el repositorio y crea un entorno virtual. Instala la librería:

```sh
pip install .
```

Para desarrollo, instálalo en modo editable:

```sh
pip install -e .
```

y ejecuta los tests:

```sh
pytest
```

## Extra: Resolver un heptagrama

> [!WARNING] 
> Usa `pyautogui` para escribir automáticamente las palabras en la ventana seleccionada.

Si quieres resolver automáticamente un hetpagrama, puedes usar el comando solve y dirigirte a la pantalla en la que está el heptagrama.

```sh
heptasolver solve --letras abdcefg --centro a
```

## Roadmap

- [] Otros diccionarios de palabras 
- [] Puntuación
 
