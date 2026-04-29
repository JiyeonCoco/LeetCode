class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 2
        pos = 2

        while pos <= len(nums)-1:
            if nums[pos] != nums[k-2]:
                nums[k] = nums[pos]
                k += 1
            pos += 1

        return k
