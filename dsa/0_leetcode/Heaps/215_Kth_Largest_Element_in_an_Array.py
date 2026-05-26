from typing import List
from collections import Counter
from collections import deque
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

        
sol = Solution()
print(sol.findKthLargest(nums =[3,2,1,5,6,4], k = 2))
