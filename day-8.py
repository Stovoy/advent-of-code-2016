"""
http://adventofcode.com/2016/day/8

--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate row x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?
"""
import re
from copy import deepcopy

rect_p = re.compile(r'rect ([0-9]+)x([0-9]+)')
row_p = re.compile(r'rotate row y=([0-9]+) by ([0-9]+)')
column_p = re.compile(r'rotate column x=([0-9]+) by ([0-9]+)')

screen = [[0 for i in range(50)] for j in range(6)]

def apply_if_rect(line):
    if not rect_p.match(line):
        return
    x, y = map(int, rect_p.match(line).groups())
    for i in xrange(x):
        for j in xrange(y):
            screen[j][i] = 1

def apply_if_row(line):
    if not row_p.match(line):
        return
    y, amount = map(int, row_p.match(line).groups())
    global screen
    new_screen = deepcopy(screen)
    for i in xrange(50):
        new_i = (i + amount) % 50
        new_screen[y][new_i] = screen[y][i]
    screen = new_screen

def apply_if_column(line):
    if not column_p.match(line):
        return
    x, amount = map(int, column_p.match(line).groups())
    global screen
    new_screen = deepcopy(screen)
    for i in xrange(6):
        new_i = (i + amount) % 6
        new_screen[new_i][x] = screen[i][x]
    screen = new_screen

with open('day-8-input.txt') as input:
    for line in input.read().splitlines():
        apply_if_rect(line)
        apply_if_row(line)
        apply_if_column(line)


print sum([sum(i) for i in screen])

"""
--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code should is the screen trying to display?
"""
for line in screen:
    for pixel in line:
        if pixel:
            print 1,
        else:
            print ' ',
    print
