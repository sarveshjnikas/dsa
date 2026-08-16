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
        r = random.random()
        # NEED BINARY SEARCH HERE... BUT I AM TIRED BOSS
        for ele in self.probs:
            if r < ele[0]:
                return ele[1]
        return 0