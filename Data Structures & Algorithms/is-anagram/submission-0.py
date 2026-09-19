class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d1 = {}

        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i] = 1

        d2 = {}

        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i] = 1
        
        
        for i in d1:
            if i not in d2 or d1[i] != d2[i]:
                return False
        
        for i in d2:
            if i not in d1 or d2[i] != d1[i]:
                return False
        print(d1,d2)

        return True
        