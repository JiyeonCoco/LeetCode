class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        outputs = []
        combine = []

        def dfs(idx):

            if sum(combine) == target:
                outputs.append(combine[:])
                return

            for i in range(idx, len(candidates)):
                num = candidates[i]

                if sum(combine+[num]) > target:
                    break

                combine.append(num)
                dfs(i)

                combine.pop()

        dfs(0)
        return outputs
