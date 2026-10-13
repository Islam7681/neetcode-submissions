class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myDict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            myDict[tuple(count)].append(s)
        return list(myDict.values())