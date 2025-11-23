class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        left_pos = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                left_pos = mid
            
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        
        left = 0
        right = len(nums) - 1
        right_pos = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                right_pos = mid
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] <= target:
                left = mid + 1

        return [left_pos, right_pos]
