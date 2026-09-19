"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return
        bfs = []
        bfs.append(node)
        visited = {}

        visited[node] = Node(node.val)

        while len(bfs):
            nnode = bfs.pop()
            
            for nn in nnode.neighbors:
                if nn not in visited:
                    bfs.append(nn)
                    visited[nn] = Node(nn.val)
                visited[nnode].neighbors.append(visited[nn])
        
        return visited[node]
                
        # ans = []
        # for i in visited.keys():
        #     ans.append(visited[i])
            # print(visited)
        return ans