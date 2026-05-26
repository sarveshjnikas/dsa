from typing import List
from collections import deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        start node A 
        --> mark A explored 
        --> now consider all nodes that could be reached from A
        --> the one with min distance can be marked explored, 
            as all other paths = something more than current + something positive
        """
        adj_list = [[] for _ in range(n+1)]   
             
        for time in times:
            adj_list[time[0]].append((time[1], time[2]))
        # print(adj_list)
        network_times = [float('inf')]*(n+1)
        network_times[k] = 0
        # print(network_times)
        
        q = []
        heapq.heappush(q, (0, k))
        while q:
            time, node = heapq.heappop(q)
            for neighbor, d in adj_list[node]:
                new_time = time + d
                if new_time < network_times[neighbor]:
                    network_times[neighbor] = new_time
                    heapq.heappush(q, (new_time, neighbor))
        ans = max(network_times[1:])
        return ans if ans != float("inf") else -1

sol = Solution()
sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
