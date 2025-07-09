import argparse
from heptasolver.domain.heptagrama import Heptagrama
from heptasolver.domain.generador import RAEGenerator
from heptasolver.infrastructure.escribiente import Escribiente
import time


def main():
    parser = argparse.ArgumentParser(description="Heptasolver")
    parser.add_argument('-l', '--letras', 
                        nargs=7, 
                        required=True, 
                        help='Las 7 letras del heptagrama, separadas por espacios (por ejemplo: a b c d e f g)')
    parser.add_argument('-c', '--centro', 
                        required=True, 
                        help='La letra central del heptagrama (por ejemplo: a)')
    args = parser.parse_args()

    heptagrama = Heptagrama(letras=args.letras, centro=args.centro)
    generador = RAEGenerator(heptagrama)
    escribiente = Escribiente()
    print(f"Resolviendo {heptagrama}")

    start_time = time.time()
    count = 0
    for palabra in generador:
        escribiente.escribir(palabra)
        count += 1
    elapsed = time.time() - start_time

    print(f"Fin - {count} palabras en {elapsed:.2f} segundos")


if __name__ == "__main__":
    main()
