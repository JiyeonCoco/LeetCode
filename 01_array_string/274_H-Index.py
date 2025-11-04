class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        h = 0

        for i, val in enumerate(citations):

            if i+1 <= val:
                h = i+1

        return h
