class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = [[0 for i in range(len(grid[0]))] for k in range(len(grid)) ]
        count = 0
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                
                if grid[row][col] == "1" and visited[row][col] == 0:
                    visited[row][col] = 1
                    bfs = []
                    bfs.append([row,col])
                    count+=1
                    while len(bfs):
                        x,y = bfs.pop()
                        
                        if x+1 < len(grid) and grid[x+1][y] == "1" and visited[x+1][y] == 0:
                            bfs.append([x+1,y])
                            visited[x+1][y] = 1
                        
                        if x-1 >= 0 and grid[x-1][y] == "1"  and visited[x-1][y] == 0:
                            bfs.append([x-1,y])
                            visited[x-1][y] = 1
                        
                        if y-1 >= 0 and grid[x][y-1] == "1"  and visited[x][y-1] == 0:
                            bfs.append([x,y-1])
                            visited[x][y-1] = 1
                        
                        if y+1 < len(grid[0]) and grid[x][y+1] == "1"  and visited[x][y+1] == 0:
                            bfs.append([x,y+1])
                            visited[x][y+1] = 1

        return count
