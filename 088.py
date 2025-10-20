class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_pos = m-1
        nums2_pos = n-1
        merge_pos = m+n-1

        while nums1_pos >= 0 and nums2_pos >= 0:
            if nums1[nums1_pos] > nums2[nums2_pos]:
                nums1[merge_pos] = nums1[nums1_pos]
                nums1_pos -= 1
            else:
                nums1[merge_pos] = nums2[nums2_pos]
                nums2_pos -= 1
            merge_pos -= 1

        nums1[:nums2_pos + 1] = nums2[:nums2_pos + 1]