from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        start = 0
        i = 0
        car_gas = 0
        while i < n:
            car_gas = car_gas + gas[i] # fill
            if car_gas < cost[i]:
                start = i + 1
                i +=1
                car_gas = 0
            else:
                car_gas = car_gas - cost[i]
                i +=1            
            
    
        return start
        