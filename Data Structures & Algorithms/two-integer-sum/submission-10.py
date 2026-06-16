class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in h and h[v] != i:
                return [h[v], i]
            h[nums[i]] = i  

