class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1_pos = m-1
        n2_pos = n-1
        add_pos = m+n-1

        while n2_pos >= 0:
            if n1_pos >= 0 and nums1[n1_pos] > nums2[n2_pos]:
                nums1[add_pos] = nums1[n1_pos]
                n1_pos -= 1
            else:
                nums1[add_pos] = nums2[n2_pos]
                n2_pos -= 1
            add_pos -= 1
