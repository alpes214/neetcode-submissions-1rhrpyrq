from collections import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets: list[list[int]] = [[] for _ in range(len(nums)+1)]
        for i, v in Counter(nums).items():
            buckets[v].append(i)

        l = []
        for i in reversed(buckets):
            l.extend(i)

        print(l)
        return l[:k]
