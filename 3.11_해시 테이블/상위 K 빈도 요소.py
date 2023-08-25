import heapq
import collections

def topKFrequent(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    print(freqs_heap)
    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

"""
def topKFrequent(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]
"""

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))
