from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # SHE CAN SEE THE ENTIRE THING AT THE BEGINNING AND CAN JUST TAKE EITHER ALL ODDS OR EVEN INDICES, WHATEVER SUMS MORE.
        return True
    
# INITIAL WRONG SOLUTINO THAT PASSED ALL CASES:
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        T = False
        if len(piles) == 2:
            return True
        else:
            T = self.stoneGame(piles[2:]) or self.stoneGame(piles[1:-1]) or self.stoneGame(piles[:-2])  
        return T