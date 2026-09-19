from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True

        d = {i : [ ] for i in range(numCourses) }
        dm = {}
        for x,y in prerequisites:
            d[x].append(y)
            # d[x] = sorted(d[x],reverse=True)
        visited = [0 for i in range(numCourses)]
        def dfs(k):
            
            if k in dm.keys():
                return dm[k]

            if visited[k] == 1:
                return False

            if d[k] == []:
                return True 

            for i in d[k]:
                visited[k] = 1
                if not dfs(i):
                    return False
                visited[k] = 0
                d[k] = []
            
            return True

        keys = list(d.keys())
        # print(d)
        for i in range(numCourses):
            # if len(d[i]) == 0:
            ans = dfs(i)
            dm[i] = ans
            if not ans:
                return False
        return True
