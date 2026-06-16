from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        nums_a = [(k, v) for k, v in c.items()]
        print(nums_a)
        nums_a.sort(key=lambda v: v[1], reverse=True)
        print(nums_a)
        l = [n[0] for n in nums_a[:k]]
        return l

        