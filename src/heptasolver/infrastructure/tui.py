import curses
import sys


def main(stdscr, solver):
    solution_is_toggled = False

    def route_command(stdscr, command):
        if command == 'q':
            sys.exit()
        if command == 's':
            toggle_solution(stdscr)
    
    def toggle_solution(stdscr):
        nonlocal solution_is_toggled
        if not solution_is_toggled: 
            stdscr.addstr(10, 0, f"Solución: {' '.join(palabras)}")
            solution_is_toggled = True
        else:
            stdscr.move(10, 0)
            stdscr.clrtoeol()
            solution_is_toggled = False

    palabras = solver.solve_all()[:3]
    encontradas = []

    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Heptagrama - Escribe ':q' para salir - ':s' para ver/tapar la solución\n")
    stdscr.addstr(1, 0, f"Letras: {' '.join(solver.heptagrama.letras)} | Centro: {solver.heptagrama.centro}\n")
    stdscr.addstr(5, 0, "Entrada: ")

    while True:
        stdscr.addstr(3, 0, f"{len(encontradas)} / {len(palabras)} palabras encontradas\n")
        
        if len(encontradas) == len(palabras):
                stdscr.move(5, 0)
                stdscr.clrtoeol()
                stdscr.addstr(5, 0, "Partida terminada! Pulsa cualquier tecla para salir :)")
                stdscr.refresh()
                stdscr.nodelay(False)
                stdscr.getch()
                break

        stdscr.move(5, 0)
        stdscr.clrtoeol()
        stdscr.addstr(5, 0, "Entrada: ")
        stdscr.refresh()
        user_input = stdscr.getstr(5, 9).decode("utf-8").strip()

        if user_input[0] == ":":
            route_command(stdscr, command=user_input[1:])
        elif user_input not in palabras:
            stdscr.move(6, 0)
            stdscr.clrtoeol()
            stdscr.addstr(6, 0, "Incorrecto!\n")
        elif user_input in encontradas:
            stdscr.move(6, 0)
            stdscr.clrtoeol()
            stdscr.addstr(6, 0, "Repetida!\n")
        else:
            encontradas.append(user_input)

            stdscr.move(6, 0)
            stdscr.clrtoeol()
            stdscr.addstr(6, 0, "")

            stdscr.move(8, 0)
            stdscr.clrtoeol()
            stdscr.addstr(8, 0, ", ".join(encontradas) + "\n")
        stdscr.refresh()
