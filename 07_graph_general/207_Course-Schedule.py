class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for sec, fir in prerequisites:
            graph[fir].append(sec)

        # 0 : 처음 보는 노드
        # 1 : 순회 중
        # 2 : 이미 순회 완료

        # visited = [0] * numCourses
        visited = {}

        def dfs(node):

            if visited.get(node) == 1:
                return False
            if visited.get(node) == 2:
                return True

            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node]= 2

            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
                
        return True

