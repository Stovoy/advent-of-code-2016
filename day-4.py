"""
# http://adventofcode.com/2016/day/4

--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""
import re

sum = 0
pattern = re.compile(r'((?:[a-z]+-)+)([0-9]+)\[([a-z]+)\]')
with open('day-4-input.txt') as input:
    for room in input.readlines():
        letters = {}
        message, sector, checksum = pattern.match(room).groups()
        message = message.replace('-', '')
        message = sorted(message)
        for char in message:
            if char in letters:
                letters[char] -= 1
            else:
                letters[char] = 1000
        letters = sorted(letters.items(), key=lambda x: (x[1], x[0]))
        fake = False
        for i in xrange(len(checksum)):
            if checksum[i] != letters[i][0]:
                fake = True
                break
        if not fake:
            sum += int(sector)
print sum

"""
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""

def rot(c, n):
    start = 97 if c.islower() else 65 if c.isupper() else False
    return chr((ord(c) - start + n) % 26 + start) if start else c

with open('day-4-input.txt') as input:
    for room in input.readlines():
        message, sector, _ = pattern.match(room).groups()
        message = message.replace('-', ' ')
        messageNew = ''
        for i in xrange(len(message)):
            messageNew += rot(message[i], int(sector))
        print messageNew, sector
