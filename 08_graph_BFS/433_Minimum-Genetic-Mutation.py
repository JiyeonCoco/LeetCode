class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        choices = ['A', 'C', 'G', 'T']

        queue = deque([(startGene, 0)])
        visited = []

        while queue:
            cur_gene, cnt = queue.popleft()

            if cur_gene == endGene:
                return cnt

            for i in range(len(cur_gene)):
                for c in choices:
                    if cur_gene[i] == c:
                        continue
                    mutation = cur_gene[:i] + c + cur_gene[i+1:]

                    if (mutation in bank) and (mutation not in visited):
                        visited.append(mutation)
                        queue.append((mutation, cnt+1))

        return -1
