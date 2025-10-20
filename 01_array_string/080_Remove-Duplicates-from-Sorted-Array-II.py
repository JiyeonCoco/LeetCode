class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1
        cnt = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
                cnt = 1
            elif (nums[i] == nums[i-1]) and (cnt < 2):
                nums[k] = nums[i]
                k += 1
                cnt += 1

        return k
