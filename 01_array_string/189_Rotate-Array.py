class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_num = len(nums)

        if k <= len(nums):
            rotate_val = nums[-k:]
        
            nums[k:] = nums[:len_num-k]
            nums[:len(rotate_val)] = rotate_val
        else:
            for i in range(k):
                cur_val = nums[-1]
                
                for j in range(len_num-1):
                    nums[len_num-j-1] = nums[len_num-j-2]
                nums[0] = cur_val
