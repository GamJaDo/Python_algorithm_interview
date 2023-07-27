import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


"""
temp = paragraph.replace(",", "").replace(".", "").lower()
result = collections.defaultdict(int)

for i in temp.split():
    if i != banned[0]:
        result[i] += 1
        
print(max(result, key=result.get))
"""

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

counts = collections.Counter(words)
print(counts.most_common(1)[0][0])
