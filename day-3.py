"""
http://adventofcode.com/2016/day/3

--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""
import re

possible_count = 0

values_pattern = re.compile(r'\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)')
with open('day-3-input.txt') as input:
    for triangle in input.readlines():
        sides = map(int, values_pattern.match(triangle).groups())
        if max(sides) < sum(sides) - max(sides):
            possible_count += 1

print possible_count

"""
--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""

# Get the triangles, then do the same loop as in part 1.
triangles = []
new_triangles = [[], [], []]
with open('day-3-input.txt') as input:
    for triangle in input.readlines():
        sides = map(int, values_pattern.match(triangle).groups())
        for i in xrange(len(sides)):
            new_triangles[i].append(sides[i])
        if len(new_triangles[0]) == 3:
            for new_triangle in new_triangles:
                triangles.append(new_triangle)
            new_triangles = [[], [], []]

possible_count = 0
for sides in triangles:
    possible = True
    if max(sides) < sum(sides) - max(sides):
        possible_count += 1

print possible_count
