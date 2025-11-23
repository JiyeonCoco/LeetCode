class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        # visited = [[0] * cols] * rows
        visited = [[0]*cols for _ in range(rows)]

        def dfs(r, c, combine, idx):

            if combine == word:
                return True

            if (r<0) or (c<0) or (r>=rows) or (c>=cols):
                return False

            if (visited[r][c]) or (board[r][c] != word[idx]):
                return False

            visited[r][c] = 1

            if dfs(r+1, c, combine+board[r][c], idx+1) or \
                dfs(r-1, c, combine+board[r][c], idx+1) or \
                dfs(r, c+1, combine+board[r][c], idx+1) or \
                dfs(r, c-1, combine+board[r][c], idx+1):
                return True

            visited[r][c] = 0

            return False


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, '', 0):
                        return True

        return False
