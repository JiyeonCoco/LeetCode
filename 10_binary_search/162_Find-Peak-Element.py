class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        max_num = nums[0]
        max_idx = 0

        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (left + right) // 2

            if mid+1 >= len(nums):
                break

            # 오르막
            if nums[mid] < nums[mid+1]:
                if mid+2 >= len(nums):
                    max_idx = mid+1
                    max_num = nums[mid+1]
                    break

                left = mid + 1

            # 내리막
            if nums[mid] > nums[mid+1]:
                right = mid - 1

                if nums[mid] >= max_num:
                    max_num = nums[mid]
                    max_idx = mid

        return max_idx
