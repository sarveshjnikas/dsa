class Solution:
    def reverse(self, x: int) -> int:
        res = -int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        return res if (res >= -2**31 or res <= 2**31 - 1) else 0
    
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1  if x>=0 else -1
        x = abs(x)
        y = 0
        while x:
            digit = x % 10
            x = x // 10
            y = y*10 + digit
            
        y = y*sign

        if (y < -2**31 or y > (2**31 - 1)):
            return 0
        
        return y
        
