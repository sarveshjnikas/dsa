from typing import List
from collections import Counter
from collections import deque
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = freq.most_common()[0:k]
        return [i for i, j in sorted_freq]
        
        
sol = Solution()
print(sol.topKFrequent(nums =[1,2,1,2,1,2,3,1,3,2], k = 2))
