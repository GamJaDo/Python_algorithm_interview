import collections

test = ["eat", "tea", "tan", "ate", "nat", "bat"]

"""
dict_t = collections.defaultdict(list)

for i in test:
    dict_t[str(sorted(i))].append(i)

result = list(dict_t.values())
for i in result:
    i.sort()

print(result)
"""

anagrams = collections.defaultdict(list)

for word in test:
    anagrams[''.join(sorted(word))].append(word)

print(list(anagrams.values()))
