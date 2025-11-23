class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap_list = []

        for num in nums:
            heapq.heappush(heap_list, num)
            if len(heap_list) > k:
                heapq.heappop(heap_list)

        return heap_list[0]
