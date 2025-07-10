import click
from heptasolver.domain.heptagrama import Heptagrama
from heptasolver.domain.generador import RAEGenerator
from heptasolver.infrastructure.escribiente import Escribiente


@click.command()
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
    raise NotImplementedError


if __name__ == "__main__":
    play()