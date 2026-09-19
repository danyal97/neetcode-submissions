class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        d = {}
        ans = 0
        while r < len(s):
            if s[r] not in d.keys():
                d[s[r]] = r
            else:
                while s[l] != s[r]:
                    del d[s[l]]
                    l+=1   
                l+=1
            r+=1
            ans = max(ans ,r-l)
        return ans

        