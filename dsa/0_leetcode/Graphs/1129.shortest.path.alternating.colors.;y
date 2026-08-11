from typing import List
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        out = [float('inf')]*(n)
        out[0] = 0
        red_adj = {}
        blue_adj = {}
        for s,d in redEdges:
            if s in red_adj:
                red_adj[s].append(d)
            else:
                red_adj[s] = [d]
        
        for s,d in blueEdges:
            if s in blue_adj:
                blue_adj[s].append(d)
            else:
                blue_adj[s] = [d]
                
        q = deque()
        visited = set()
        
        if 0 in red_adj:
            for r in red_adj[0]:
                out[r] = 1 if r !=0 else out[r]
                q.append((r, "r", 1))
                visited.add((0, "r", r))
                
            
        if 0 in blue_adj:
            for b in blue_adj[0]:
                out[b] = 1 if b != 0 else out[b]
                q.append((b, "b", 1))
                visited.add((0, "b", b))
        
        while q:
            node, color, cost = q.popleft()
            if color == "b" and node in red_adj:
                for next in red_adj[node]:
                    out[next] = min(out[next], cost+1)
                    if (node, "r", next) not in visited:
                        q.append((next, "r", cost+1))
                        visited.add((node, "r", next))
                
            if color == "r" and node in blue_adj:
                for next in blue_adj[node]:
                    out[next] = min(out[next], cost+1)
                    if (node, "b", next) not in visited:
                        q.append((next, "b", cost+1))
                        visited.add((node, "b", next))

        for i in range(len(out)):
            if out[i] == float('inf'):
                out[i] = -1
        return out
        