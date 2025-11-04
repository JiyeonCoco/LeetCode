class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 왼쪽 순회 / 오른쪽 순회하면 손쉽게 구할 수 있음
        n = len(nums)
        res = [1] * n
        
        # 1️⃣ 왼쪽 곱 계산
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        # 2️⃣ 오른쪽 곱 계산 및 합치기
        right = 1
        for i in reversed(range(n)):
            res[i] *= right
            right *= nums[i]
        
        return res
