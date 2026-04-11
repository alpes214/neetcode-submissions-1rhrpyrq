from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        target = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in target[:k]]

