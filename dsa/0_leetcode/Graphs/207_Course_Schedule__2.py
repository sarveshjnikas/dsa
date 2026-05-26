from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        find courses that have no prerequisites --> take them
        does taking that course free up any other courses ? yes --> take them
        in the end count the number of courses you were able to take 
        """
        
        indegree = [0]*numCourses # how many courses does the course needs
        graph = [[] for _ in range(numCourses)] # courses that need the particular course as prerequisite

        for course, prerequisite in prerequisites:
            indegree[course] += 1
            graph[prerequisite].append(course)
        
        q = deque()
        taken = 0 
        order = []
        
        for i in range(numCourses):
            if indegree[i] == 0:
                order.append(i)
                q.append(i)
                
        while q:
            node = q.popleft()
            taken += 1
            for nei in graph[node]:
                indegree[nei] -= 1 
                if indegree[nei] == 0: 
                    order.append(nei)
                    q.append(nei)
        return order if taken == numCourses else []
        
sol = Solution()
sol.canFinish(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
