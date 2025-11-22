class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # ===================================== #
        # ================ BFS ================ #
        # ===================================== #
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for sec, fir in prerequisites:
            graph[fir].append(sec)
            in_degree[sec] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        cnt = 0

        while queue:
            node = queue.popleft()
            cnt += 1
            
            for nei in graph[node]:
                in_degree[nei] -= 1

                if in_degree[nei] == 0:
                    queue.append(nei)

        if cnt == numCourses:
            return True
        return False




        # ===================================== #
        # ================ DFS ================ #
        # ===================================== #
        
        # graph = defaultdict(list)

        # for sec, fir in prerequisites:
        #     graph[fir].append(sec)

        # # 0 : 처음 보는 노드
        # # 1 : 순회 중
        # # 2 : 이미 순회 완료

        # # visited = [0] * numCourses
        # visited = {}

        # def dfs(node):

        #     if visited.get(node) == 1:
        #         return False
        #     if visited.get(node) == 2:
        #         return True

        #     visited[node] = 1
        #     for nei in graph[node]:
        #         if not dfs(nei):
        #             return False
        #     visited[node]= 2

        #     return True

        # for n in range(numCourses):
        #     if not dfs(n):
        #         return False
                
        # return True

