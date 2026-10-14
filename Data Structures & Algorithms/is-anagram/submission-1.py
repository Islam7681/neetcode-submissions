class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        myDict1 = {}
        myDict2 = {}

        for i in range(len(s)):
            myDict1[s[i]] = 1 + myDict1.get(s[i], 0)
            myDict2[t[i]] = 1 + myDict2.get(t[i], 0)
        return myDict1 == myDict2