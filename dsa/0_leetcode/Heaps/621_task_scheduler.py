import heapq
from typing import List
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for v in counts.values() if v == max_freq)
        c = (max_freq-1)*(n+1) + max_count
        return max(c, len(tasks))
        
