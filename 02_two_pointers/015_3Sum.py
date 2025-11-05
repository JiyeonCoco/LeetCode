class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 중복 방지를 위한 전처리가 중요한 문제

        if len(nums) < 3:
            return []
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        output = []
        nums.sort()

        # 중복 방지를 위해 left, right를 뺀 -2만큼만 조회
        for i, s in enumerate(nums[:-2]):

            # 중복 방지
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:

                sum_num = nums[left] + nums[right]

                if sum_num == s * -1:
                    cur_triplets = [s, nums[left], nums[right]]
                    output.append(cur_triplets)

                    # 중복 방지
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif sum_num < s * -1:
                    left += 1
                elif sum_num > s * -1:
                    right -= 1

        return output
