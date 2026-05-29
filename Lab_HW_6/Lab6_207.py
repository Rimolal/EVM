class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        state = [0] * numCourses
        
        def dfs(course: int) -> bool:
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            state[course] = 1
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2
            return True
        
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False
        
        return True