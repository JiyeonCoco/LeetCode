class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        end = 0
        max_reach = 0

        for i, jump in enumerate(nums[:-1]):
            max_reach = max(max_reach, i+jump)

            if i == end:
                jumps += 1
                end = max_reach

        return jumps

        
