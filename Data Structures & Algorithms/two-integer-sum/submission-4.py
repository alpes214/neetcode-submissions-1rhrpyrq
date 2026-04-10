class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {} # v : i
        for i, v in enumerate(nums):
            diff = target - v
            if diff in values:
                return [values[diff], i]
            values[v] = i
        return
