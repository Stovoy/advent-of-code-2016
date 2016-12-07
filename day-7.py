"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?
"""

def is_tls(chars):
    for i in xrange(len(chars)):
        four = chars[i:i+4]
        if len(four) != 4:
            return False
        if four[0] == four[3] and four[1] == four[2] and four[0] != four[1]:
            return True

count = 0
in_brackets = False
with open('day-7-input.txt') as input:
    for line in input.read().splitlines():
        abba_in_hypernet = False
        valid_abba = False
        chars = ''
        for c in line:
            if c == '[':
                if is_tls(chars):
                    valid_abba = True
                chars = ''
            elif c == ']':
                if is_tls(chars):
                    abba_in_hypernet = True
                    break
                chars = ''
            else:
                chars += c
        if not abba_in_hypernet and (valid_abba or is_tls(chars)):
            count += 1

print count

"""
--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
How many IPs in your puzzle input support SSL?
"""
def get_aba_list(chars):
    aba_list = []
    for i in xrange(len(chars)):
        aba = chars[i:i+3]
        if len(aba) != 3:
            return aba_list
        if aba[0] == aba[2] and aba[0] != aba[1]:
            aba_list.append(aba)

def test_bab(chars, aba_list):
    for i in xrange(len(chars)):
        bab = chars[i:i+3]
        if len(bab) != 3:
            return False
        for aba in aba_list:
            if bab[0] == aba[1] and bab[1] == aba[0] and bab[2] == aba[1]:
                return True

count = 0
with open('day-7-input.txt') as input:
    for line in input.read().splitlines():
        aba_chars = ''
        bab_chars = ''
        in_brackets = False
        for c in line:
            if c == '[':
                in_brackets = True
            elif c == ']':
                in_brackets = False
            elif not in_brackets:
                aba_chars += c
            elif in_brackets:
                bab_chars += c
        aba_list = get_aba_list(aba_chars)
        if test_bab(bab_chars, aba_list):
            count += 1

print count
