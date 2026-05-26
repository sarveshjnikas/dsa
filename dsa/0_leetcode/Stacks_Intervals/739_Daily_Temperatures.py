from typing import List
from collections import Counter

class Solution:
    # brute force solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        answer = []
        i = 0
        for i in range(0, len(temperatures)):
            t = temperatures[i]
            j = i +1
            while j < len(temperatures):
                if temperatures[j] > t:
                    answer.append(j-i)
                    break
                else:
                    j = j+1
            
            answer.append(0) if j == len(temperatures) else None
            
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = n*[0]
        
        # we try to store "unresolved" temperatures. 
        # for each new temperature we see, try to ask what temperatures does it resolve. 
        unresolved = [[0,temperatures[0]]]
        resolved = []
        for i in range(1,n):
            # check if the temperature resolves anything
            current_temp = temperatures[i]
            id = 0
            while id < len(unresolved):
                unres = unresolved[id]
                if unres[1] < current_temp:
                    unresolved.pop(id)
                    unres.append(i)
                    resolved.append(unres)
                else:
                    id +=1
            unresolved.append([i,temperatures[i]])
            
        unres_res = [(i,0) for i, _ in unresolved] + [(i, j - i) for i, _, j in resolved]
        
        for i, val in unres_res:
            answer[i] = val
        return answer
    
    ##################
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = []
        
        for i in range(0, len(temperatures)):
            current_temperature = temperatures[i]
            while stack and temperatures[stack[-1]] < current_temperature:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        
        return answer
        
sol = Solution()
print(sol.dailyTemperatures(temperatures =[73,74,75,71,69,72,76,73]))
