import curses

def main(stdscr, solver):
    
    palabras = solver.solve_all()[:3]
    encontradas = []

    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Heptagrama - Escribe ':q' para salir\n")
    stdscr.addstr(1, 0, f"Letras: {' '.join(solver.heptagrama.letras)} | Centro: {solver.heptagrama.centro}\n")
    stdscr.addstr(5, 0, "Entrada: ")
    stdscr.addstr(10, 0, f"Solución: {' '.join(palabras)}")

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

        if user_input == ":q":
            break

        if user_input not in palabras:
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
