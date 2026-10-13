class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myDict = {}

        for n in nums:
            myDict[n] = 1 + myDict.get(n, 0)

        bucket_list = [[] for i in range(len(nums) +1)]

        for num, cnt in myDict.items():
            bucket_list[cnt].append(num)

        res = []

        for i in range(len(bucket_list) - 1, 0, -1):
            for num in bucket_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
