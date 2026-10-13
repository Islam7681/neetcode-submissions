class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ourMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in ourMap:
                return [ourMap[difference], i]
            ourMap[n] = i
