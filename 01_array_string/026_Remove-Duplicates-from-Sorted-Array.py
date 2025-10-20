class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        uniq_vals = []

        for i in range(len(nums)):
            if nums[i] not in uniq_vals:
                nums[k] = nums[i]
                k += 1
                uniq_vals.append(nums[i])

        return k

