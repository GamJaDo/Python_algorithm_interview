import collections


def numJewelsInStones(J, S):
    freqs = {}
    count = 0

    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    for char in J:
        if char in freqs:
            count += freqs[char]

    return count

"""
def numJewelsInStones(J, S):
    freqs = collections.defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1

    for char in J:
        count += freqs[char]

    return count
    

def numJewelsInStones(J, S):
    freqs = collections.Counter(S)
    count = 0

    for char in J:
        count += freqs[char]

    return count


def numJewelsInStones(J, S):
    return sum(s in J for s in S)
"""

J = "aA"
S = "aAAbbbb"

print(numJewelsInStones(J, S))
