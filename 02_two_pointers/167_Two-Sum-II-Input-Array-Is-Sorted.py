class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # 이중 반복문으로 하게 되면 시간복잡도가 많이 증가함
        # 오름차순 정렬이 되어있다 라는 점을 이용하여 left/right 로 나누어 계산 및 순회
        
        n1 = 0
        n2 = len(numbers)-1

        while n1 <= n2:

            sum_num = numbers[n1]+numbers[n2]

            if sum_num == target:
                return [n1+1, n2+1]

            elif sum_num < target:
                n1 += 1

            elif sum_num > target:
                n2 -= 1
