from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = 26
        def enc(letter):
            return ord(letter)- ord('a')
        
        minimum_cost = [[float('inf')]*n for _ in range(n)]
        
        for i in range(n):
            minimum_cost[i][i] = 0
        
        for j in range(len(original)):
            senc = enc(original[j])
            tenc = enc(changed[j])
            minimum_cost[senc][tenc] = min(cost[j], minimum_cost[senc][tenc])
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    minimum_cost[i][j] = min(minimum_cost[i][j], minimum_cost[i][k]+ minimum_cost[k][j])
                    
        i = 0
        total_cost = 0   
        while i < len(source): 
            while i< len(source) and source[i] == target[i]:
                i += 1
                
            if i < len(source):
                senc = enc(source[i])
                tenc = enc(target[i])
                if minimum_cost[senc][tenc] == float('inf'):
                    return -1
                else:
                    total_cost = total_cost + minimum_cost[senc][tenc]
                i += 1
        return total_cost