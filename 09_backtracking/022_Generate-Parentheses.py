class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        outputs = []

        def dfs(combine, left, right):

            if len(combine) == n*2:
                outputs.append(combine)
                return

            if left < n:
                dfs(combine + '(', left+1, right)
            
            if right < left:
                dfs(combine + ')', left, right+1)

        dfs("", 0, 0)

        return outputs
