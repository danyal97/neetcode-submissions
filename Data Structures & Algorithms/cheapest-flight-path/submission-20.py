from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        d = defaultdict(list)

        for i,j,cost in flights:
            d[i].append([j,cost])

        def dfs(node,c,a,ans):
            if c > ans:
                return ans
            if node == dst and len(a) <= k+2:
                ans = min(ans,c)
                return ans
            for i,cost in d[node]:
                if i not in a:
                    ans = dfs(i, c+cost, a+[i], ans)

            return ans

        ans = dfs(src,0,[src], 999999)
        if ans == 999999:
            return -1
        return ans