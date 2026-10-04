class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def rec(x, y, i):

            if board[x][y] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < len(board) and
                    0 <= ny < len(board[0]) and
                    not visited[nx][ny]):

                    visited[nx][ny] = 1
                    if rec(nx, ny, i + 1):
                        return True
                    visited[nx][ny] = 0

            return False
        
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):

                visited[i][j] = 1
                if rec(i,j, 0):
                    return True
                visited[i][j] = 0
        
        return False