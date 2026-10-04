from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        d = defaultdict(list)

        for i,j in edges:
            d[i].append(j)
            d[j].append(i)

        visited = [0 for i in range(n)]
        def rec(node, prev):
            if visited[node] == 1:
                return False
            visited[node] = 1
            for i in d[node]:
                if i == prev:
                    continue
                if rec(i, node) == False:
                    return False
            return True

        return rec(0,-1) and (n == sum(visited))