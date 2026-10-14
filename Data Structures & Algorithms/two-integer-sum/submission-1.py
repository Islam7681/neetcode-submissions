class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myDict = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in myDict:
                return [myDict[difference], i]
            myDict[n] = i