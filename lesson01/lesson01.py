import curses
import time


def draw(canvas):
    row, column = (5, 20)
    canvas.addstr(row, column, 'Hello, world!', curses.A_REVERSE | curses.A_BOLD)
    curses.curs_set(False)
    canvas.attron(curses.A_BOLD)
    canvas.border('L','R','T','B','*','*','*','*')
    canvas.attron(curses.A_NORMAL)
    canvas.refresh()
    time.sleep(10)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
