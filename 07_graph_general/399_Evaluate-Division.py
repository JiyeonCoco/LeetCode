class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for idx, (A, B) in enumerate(equations):
            graph[A].append((B, values[idx]))
            graph[B].append((A, (1 / values[idx])))

        def dfs(start, end, visited, output):

            if start not in graph:
                return -1

            if start == end:
                return 1

            visited.append(start)
            for dst, weight in graph[start]:
                if dst not in visited:
                    res = dfs(dst, end, visited, output)
                    if res != -1:
                        return res * weight

            return -1
        
        results = []
        for idx, (C, D) in enumerate(queries):
            visited = []
            output = 1
            cur_result = dfs(C, D, visited, output)
            results.append(cur_result)

        return results
