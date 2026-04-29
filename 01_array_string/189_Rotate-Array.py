class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        right_num = nums[-k:]

        pos = len(nums)-1

        for i in range(len(nums)-k-1, -1, -1):
            nums[pos] = nums[i]
            pos -= 1

        for idx, r in enumerate(right_num):
            nums[idx] = r
