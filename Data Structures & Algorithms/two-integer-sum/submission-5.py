class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {} # v: i
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hash_nums:
                return [hash_nums[diff], i]
            hash_nums[v] = i
        return []
