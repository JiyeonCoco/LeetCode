class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # 일단 총 연료가 충분한지 1차 필터링. 여기에서 걸리지 않으면 순회가 가능하다는 의미
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        start_pos = 0

        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            if tank < 0:
                tank = 0
                start_pos = i+1

        return start_pos
