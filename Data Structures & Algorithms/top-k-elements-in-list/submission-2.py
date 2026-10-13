class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myDict = {}
        for i in nums:
            myDict[i] = 1 + myDict.get(i, 0)
        
        bucket_list = [[] for i in range(len(nums)+1)]
        for num, cnt in myDict.items():
            bucket_list[cnt].append(num)
        
        res = []
        for n in range(len(bucket_list) -1, 0, -1):
            for num in bucket_list[n]:
                res.append(num)
                if len(res) == k:
                    return res