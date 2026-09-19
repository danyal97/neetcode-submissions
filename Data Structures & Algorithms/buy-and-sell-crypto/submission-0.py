class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        ans = 0
        while l!=r and r <= len(prices) - 1:
            # print(l,r)
            while l <=r and prices[l] > prices[r]:
                l+=1
            ans = max(ans, prices[r] - prices[l])
            r+=1
        return (ans)