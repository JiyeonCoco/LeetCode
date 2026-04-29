class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        right = [1] * len(nums)

        for idx in range(1, len(nums)):
            left[idx] = left[idx-1] * nums[idx-1]

        for idx in range(len(nums)-2, -1, -1):
            right[idx] = right[idx+1] * nums[idx+1]

        results = left.copy()
        for idx in range(len(right)):
            results[idx] *= right[idx]

        return results
