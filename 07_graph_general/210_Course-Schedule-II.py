class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # =================================== #
        # =============== BFS =============== #
        # =================================== #

        graph = defaultdict(list)
        in_degree = [0] * numCourses
        course = []

        for sec, fir in prerequisites:
            graph[fir].append(sec)
            in_degree[sec] += 1

        # queue = deque()
        # for i in range(numCourses):
        #     if in_degree[i] == 0:
        #         queue.append(i)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            course.append(node)

            for nei in graph[node]:
                in_degree[nei] -= 1

                if in_degree[nei] == 0:
                    queue.append(nei)

        if len(course) == numCourses:
            return course
            
        return []


        # =================================== #
        # =============== DFS =============== #
        # =================================== #
        # graph = defaultdict(list)

        # for sec, fir in prerequisites:
        #     graph[fir].append(sec)

        # course = []
        # # 0 : 아직 안 봄
        # # 1 : 순회 중
        # # 2 : 순회 완료
        # visited = {}
        # self.hasCycle = False

        # def dfs(node):

        #     if self.hasCycle:
        #         return

        #     if visited.get(node) == 1:
        #         self.hasCycle = True
        #         return

        #     if visited.get(node) == 2:
        #         return

        #     visited[node] = 1

        #     for nei in graph[node]:
        #         dfs(nei)

        #     visited[node] = 2
        #     course.append(node)


        # for n in range(numCourses):
        #     if (n not in visited) or (visited.get(n) == 0):
        #         dfs(n)

        # if self.hasCycle:
        #     return []
        # return course[::-1]
