import click
import time
import keyboard
from heptasolver.domain.entities.heptagrama import Heptagrama
from heptasolver.domain.services.generador import RAEGenerator
from heptasolver.infrastructure.escribiente import Escribiente


@click.command(help="Resolver un heptagrama")
@click.option(
    '-l', '--letras',
    required=True,
    help='Las 7 letras del heptagrama (p.e. --letras abcdefg)'
)
@click.option(
    '-c', '--centro',
    required=True,
    help='La letra central del heptagrama (p.e. --centro a)'
)
def solve(letras, centro):
    if len(letras) != 7:
        click.echo(f"{letras=}, {len(letras)=}")
        raise click.BadParameter("Debes proporcionar exactamente 7 letras para el heptagrama.")

    letras = list(letras)
    heptagrama = Heptagrama(letras=letras, centro=centro)
    generador = RAEGenerator(heptagrama)
    escribiente = Escribiente()
    click.echo(f"Resolviendo {heptagrama}. Pulsa cualquier ESC para salir.")

    start_time = time.time()
    count = 0
    for palabra in generador:
        escribiente.escribir(palabra)
        if keyboard.is_pressed('esc'):
            #TODO: Esto no funciona muy bien
            print("Abortando...")
            break
        count += 1
    elapsed = time.time() - start_time

    click.echo(f"Fin - {count} palabras en {elapsed:.2f} segundos")

if __name__ == "__main__":
    solve()

