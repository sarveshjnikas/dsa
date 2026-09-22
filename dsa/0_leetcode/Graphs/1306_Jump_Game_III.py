from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        m = len(arr)
        q = deque([start])
        visited= {start}
        
        while q:
            node = q.popleft()
            if arr[node] ==0:
                return True
            visited.add(node)
            for j in (node + arr[node], node - arr[node]):
                if 0 <= j < m and j not in visited:
                    visited.add(j)
                    q.append(j)
        return False
        
        
sol = Solution()
sol.canReach(arr = [4,2,3,0,3,1,2], start = 0)
