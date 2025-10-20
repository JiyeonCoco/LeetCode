class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # ===================================== #
        # ====== Sol 1 (proc time: 19ms) ====== #
        # ===================================== #
        # k = 0
        # uniq_vals = []

        # for i in range(len(nums)):
        #     if nums[i] not in uniq_vals:
        #         nums[k] = nums[i]
        #         k += 1
        #         uniq_vals.append(nums[i])

        # return k

        # ==================================== #
        # ====== Sol 2 (proc time: 3ms) ====== #
        # ==================================== #
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k
