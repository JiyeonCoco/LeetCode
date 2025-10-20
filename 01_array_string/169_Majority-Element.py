class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # ============================= #
        # === Sol 1 (runtime: 19ms) === #
        # ============================= #
        # maj_dict = {nums[0]: 1}

        # for i in nums[1:]:
        #     if i not in maj_dict.keys():
        #         maj_dict[i] = 1
        #     else:
        #         maj_dict[i] += 1

        # return max(maj_dict, key=maj_dict.get)


        # ============================= #
        # === Sol 1 (runtime: 7ms) === #
        # ============================= #
        cnt = 0
        maj = None

        for i in nums:

            if cnt == 0:
                maj = i
                
            if i == maj:
                cnt += 1
            else:
                cnt -= 1

        return maj
                

