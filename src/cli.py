import click
from heptasolver.application.solve import solve
from heptasolver.application.play import play


@click.group()
def cli():
    pass


cli.add_command(solve)
cli.add_command(play)
