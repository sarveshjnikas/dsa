from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = [[0]*numCourses for _ in range(numCourses)]
        for k in prerequisites:
            dep[k[0]][k[1]] = 1
        
        for k in range(numCourses):
            for j in range(numCourses):
                if dep[k][j] == 1:
                    for l in range(numCourses):
                        if dep[j][l] == 1:
                            dep[k][l] = 1
                
        for _ in range(numCourses):
            if dep[_][_] ==1:
                return False
        return True
        
        
sol = Solution()
sol.canFinish(numCourses = 4, prerequisites = [[0,1],[1,0],[1,3], [0,2]])
