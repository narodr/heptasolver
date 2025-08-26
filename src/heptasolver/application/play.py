import click
import curses
import sys
from heptasolver.domain.services.solver import Solver
from heptasolver.infrastructure import tui
from heptasolver.infrastructure import utils


@click.command(help="Inicia una partida")
@click.option(
    '-l', '--letras',
    required=False,
    help='Las 7 letras del heptagrama (p.e. --letras abcdefg)'
)
@click.option(
    '-c', '--centro',
    required=False,
    help='La letra central del heptagrama (p.e. --centro a)'
)
def play(letras, centro):
    playable = False
    if (letras and centro):
        solver = Solver(letras=letras, centro=centro)
        if not solver.is_playable():
            print("Not playable. Try another combination of letters and center")
            sys.exit()
    elif (letras and not centro):
        while not playable:
            for letra in letras:
                centro = letra
                solver = Solver(letras=letras, centro=centro)
                playable = solver.is_playable()
    elif (not letras and centro):
        while not playable:
            letras = utils.get_random_letters(centro)
            solver = Solver(letras=letras, centro=centro)
            playable = solver.is_playable()
    else:
        while not playable:
            centro = utils.get_random_center()
            letras = utils.get_random_letters(centro)
            solver = Solver(letras=letras, centro=centro)
            playable = solver.is_playable()

    curses.wrapper(tui.main, solver)


if __name__ == "__main__":
    play()