from typing import List
from collections import Counter
from collections import deque
import heapq

class Solution:
    def isHappy(self, n: int) -> bool:
        ini = n
        num = n
        while True:
            num = sum([int(i)**2 for i in str(n)])
            # print(n, num)
            if num ==1:
                return True
            
            if len(str(num)) == 1:
                print(str(num))
                if str(num) not in ["1","7"]:
                    return False
                else: 
                    return True
            n = num 
        

sol = Solution()
print(sol.isHappy(1111111))
