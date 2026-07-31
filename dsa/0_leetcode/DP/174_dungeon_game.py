from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon), len(dungeon[0])
        health = [[float('inf')]*n for _ in range(m)] # health we need before entering the cell
        health[-1][-1] = max(1, 1-dungeon[-1][-1])

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    continue
                print(dungeon[i][j])
                # where can i go from (i,j) --> (i+1, j) or (i,j+1)
                hp1 = health[i][j+1] if j+1 < n else float('inf') # health needed at i,j+1
                hp2 = health[i+1][j] if i+1 < m else float('inf') # health needed at i+1, j
                
                hpn1 = 1 if dungeon[i][j] >= hp1 else hp1-dungeon[i][j] # health needed before entering i,j in order to surive at i,j+1
                hpn2 = 1 if dungeon[i][j] >= hp2 else hp2-dungeon[i][j]  # health needed before entering i,j in order to surive at i+1,j
                
                health[i][j] = min(hpn1, hpn2)
                    
        return health[0][0]