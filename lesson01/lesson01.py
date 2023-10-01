import curses
import time
import asyncio
import random

TIC_TIMEOUT = 0.1


async def go_to_sleep(seconds):
    iteration_count = int(seconds * 10)
    for _ in range(iteration_count):
        await asyncio.sleep(0)


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await go_to_sleep(2)

        canvas.addstr(row, column, symbol)
        await go_to_sleep(0.3)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await go_to_sleep(0.5)

        canvas.addstr(row, column, symbol)
        await go_to_sleep(0.3)


def draw(canvas):
    max_y, max_x = canvas.getmaxyx()
    curses.curs_set(False)
    canvas.border(0, 0, 0, 0, 0, 0, 0, 0)
    coroutines = []
    stars = '+*.:'
    for i in range(100):
        row = random.randint(2, max_y-2)
        column = random.randint(2, max_x-2)
        coroutine = blink(canvas, row, column, random.choice(stars))
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
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
