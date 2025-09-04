[![es](https://img.shields.io/badge/README-ES-dodgerblue)](README.es.md)

Play or solve a [heptagram](https://elpais.com/juegos/heptagrama/)

> Starting from seven letters arranged in a hexagonal shape, with one of them in the 
central position, the objective is to form the maximum number of words with at least 
three letters.
You can repeat letters, but you must always include the one in the central position. 
Proper nouns, plurals, and conjugated verb forms (only infinitives) are not allowed.

### Play a game

You can play a game through the terminal by running the play command. Optionally you can specify the center or the letters you want to play.

```sh
heptasolver play [-l abcdefg] [-c a]
```

## Install

Clone the repo and (optionally) create a virtual environment. Then install the package: 

```sh
pip install .
```

For developers, install it in editable mode:
    
```sh
pip install -e .
```

and execute tests:

```sh
pytest
```

## Extra: Solve

> [!WARNING] 
> This command use `pyautogui` to automatically write words in the selected window.

To solve a heptagram, execute

```sh
heptasolver solve --letras abdcefg --centro a
```

then move to the target window.
