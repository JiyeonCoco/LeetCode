class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        queue = deque([(1, 0)])
        visited = set()
        visited.add(1)
        n = len(board)
        
        def get_pos(num):
            quot, rem = divmod(num-1, n)
            r = n - 1 - quot
            if (n - 1 - r) % 2 == 0:
                c = rem
            else:
                c = n - 1 - rem
            return r, c

        while queue:
            pos, cnt = queue.popleft()

            if pos == n*n:
                return cnt
            
            roll_range = min(7, n*n-pos+1)

            for i in range(1, roll_range):

                dst = pos + i
                r, c = get_pos(dst)

                if board[r][c] != -1:
                    dst = board[r][c]
                
                if dst not in visited:
                    visited.add(dst)
                    queue.append((dst, cnt+1))

        return -1



