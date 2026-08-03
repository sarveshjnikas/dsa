from collections import deque
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = 0
        left = 0
        right = len(people)-1
        dq = deque(people)

        while dq:
            if left == right:
                return boats +1
                
            if dq[left] + dq[right] <= limit:
                boats += 1
                dq.pop()
                dq.popleft()
                left = 0
                right = len(dq)-1
            elif dq[left] + dq[right] > limit:
                boats +=1
                dq.popleft()
                right = right-1