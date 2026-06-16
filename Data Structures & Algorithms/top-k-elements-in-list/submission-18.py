from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        nums_a = [(k, v) for k, v in c.items()]
        nums_a.sort(key=lambda v: v[1], reverse=True)
        l = [n[0] for n in nums_a[:k]]
        return l

        