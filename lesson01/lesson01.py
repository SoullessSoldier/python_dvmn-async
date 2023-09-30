import curses
import time
import asyncio


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


def draw(canvas):
    row, column = (3, 10)
    curses.curs_set(False)
    canvas.border(0, 0, 0, 0, 0, 0, 0, 0)
    coroutines = []
    for i in range(5):
        coroutine = blink(canvas, row, column+i)
        coroutines.append(coroutine)
    # print('type', type(coroutine))
    # print('dir', dir(coroutine))
    # time.sleep(5)
    while True:
        # canvas.addstr(row, column, '*', curses.A_DIM)
        # canvas.refresh()
        # time.sleep(2)
        # canvas.addstr(row, column, '*')
        # canvas.refresh()
        # time.sleep(0.3)
        # canvas.addstr(row, column, '*', curses.A_BOLD)
        # canvas.refresh()
        # time.sleep(0.5)
        # canvas.addstr(row, column, '*')
        # canvas.refresh()
        # time.sleep(0.3)
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                print('stop iteration')
        canvas.refresh()
        time.sleep(1)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
