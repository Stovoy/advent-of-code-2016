"""
# http://adventofcode.com/2016/day/1

--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?
"""
import operator

instructions = 'R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'

heading = 0

left = {
    0: 3,  # north -> west
    1: 0,  # east -> north
    2: 1,  # south -> east
    3: 2,  # west -> south
}
right = {
    0: 1,  # north -> east
    1: 2,  # east -> south
    2: 3,  # south -> west
    3: 0,  # west -> north
}
step = {
    0: (0, 1),   # north + 1
    1: (1, 0),   # east + 1
    2: (0, -1),  # south + 1
    3: (-1, 0),  # west + 1
}

loc = (0, 0)

instructions = instructions.replace(' ', '').split(',')
for instruction in instructions:
    heading = left[heading] if instruction[0] == 'L' else right[heading]
    distance = int(instruction[1:])
    move = tuple(distance * coord for coord in step[heading])
    loc = tuple(map(operator.add, loc, move))

print sum(map(abs, loc))

"""
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

# Note: Not clear whether being between two instructions counts as visiting. Assumed no at first and was wrong.

loc = (0, 0)
visited = set()
for instruction in instructions:
    heading = left[heading] if instruction[0] == 'L' else right[heading]
    distance = int(instruction[1:])
    found = False
    for i in xrange(distance):  # Go one step at a time and check visited.
        loc = tuple(map(operator.add, loc, step[heading]))
        if loc in visited:
            found = True
            break
        visited.add(loc)
    if found:
        break

print sum(map(abs, loc))
