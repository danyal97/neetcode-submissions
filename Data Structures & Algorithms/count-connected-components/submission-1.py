from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        d = defaultdict(list)

        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        
        visited = [0 for i in range(n)]
        def dfs(node, prev):
            if visited[node] == 1:
                return
            
            visited[node] = 1

            for i in d[node]:
                if i==prev:
                    continue
                dfs(i, node)
        
        print()
        count = 0

        for k in range(n):
            if visited[k] == 0:
                dfs(k,-1)
                count+=1
        return (count)

        
        