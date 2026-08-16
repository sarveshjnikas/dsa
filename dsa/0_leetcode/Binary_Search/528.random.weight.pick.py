from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.probs = []
        p = 0
        for i in range(len(w)):
            p = p + w[i]/total
            self.probs.append((p, i))
            
    def pickIndex(self) -> int:
        R = random.random()        
        l = 0
        r = len(self.probs)-1
        while l <= r:
            mid = l + (r-l)//2
            below = 0 if mid ==0 else self.probs[mid-1][0]
            if below <= R  <= self.probs[mid][0]:
                return self.probs[mid][1]
            
            if R > self.probs[mid][0]:
                l = mid + 1
            else:
                r = mid -1
            
        return 0