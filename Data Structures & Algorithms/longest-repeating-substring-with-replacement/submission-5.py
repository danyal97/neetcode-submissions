class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        maxfq = 0
        d = {}
        r = 0
        ans = 0

        while r < len(s):
            # print(d.values())
            if s[r] in d.keys():
                d[s[r]]+=1
            else:
                d[s[r]] = 1
            
            maxfq = max(maxfq, max(d.values()) )
            
            if (r-l+1) - maxfq <= k:
                ans = max(ans, r-l+1)
            else:
                while (r-l+1) - max(d.values()) > k:
                    d[s[l]]-=1
                    l+=1
            r+=1
        return ans



                  
        