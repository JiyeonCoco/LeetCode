class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        outputs = []
        k = len(nums)
        visited = [0] * k

        def dfs(combine):

            if len(combine) == k:
                outputs.append(combine[:])
                return

            for i, n in enumerate(nums):
                if visited[i] == 0:
                    visited[i] = 1
                    dfs(combine+[n])
                    visited[i] = 0

        dfs([])

        return outputs
