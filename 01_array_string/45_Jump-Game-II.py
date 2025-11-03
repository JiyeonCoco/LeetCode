class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        end = 0
        max_reach = 0

        # end : 지금 한 번 점프해서 닿을 수 있는 범위
        # max_reach : 다음에 점프할 때 가장 멀리 갈 수 있는 지점

        for i, jump in enumerate(nums[:-1]):
            max_reach = max(max_reach, i+jump)

            if i == end:
                jumps += 1
                end = max_reach

        return jumps

        
