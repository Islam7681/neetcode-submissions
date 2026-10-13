class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myDict = {}
        for i in nums:
            myDict[i] = 1 + myDict.get(i, 0)

        bucket_list = [[] for i in range(len(nums) + 1)]
        for nums, cnt in myDict.items():
            bucket_list[cnt].append(nums)

        result = []
        for i in range(len(bucket_list)-1, 0, -1):
            for num in bucket_list[i]:
                result.append(num)
                if  len(result) == k:
                    return result
