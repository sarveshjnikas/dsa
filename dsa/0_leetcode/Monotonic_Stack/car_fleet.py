class Solution:
    def carFleet(self, target, position, speed) -> int:
        concat = [(x, v, (target-x)/v) for x, v in zip(position, speed)]
        concat.sort(key=lambda p:p[0],reverse=True)
        fleets = 1
        start = 0
        for i in range(1, len(concat)):
            time_current = concat[i][2]
            time_limiting = concat[start][2]
            if time_current > time_limiting: # can not catch up to the car ahead
                fleets +=1
                start = i
        return fleets
