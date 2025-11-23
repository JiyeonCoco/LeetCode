class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        outputs = []
        
        def dfs(num, state):

            if len(state) == k:
                outputs.append(state)
                return

            for i in range(num, n+1):
                dfs(i+1, state+[i])

        dfs(1, [])

        return outputs
