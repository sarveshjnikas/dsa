"""
Need to understand some basics first:

5 = 101
in a 8 bit machine: 5 = 00000101
How are negative numbers stored?
two complement
00000101 start with 5
11111010 flip bits
11111011 add 1

largest positive:
01111111 = 127

most negative:
10000000 = -128

unsigned:
11111011
= 128+64+32+16+8+2+1
= 251

signed two's complement,
11111011
= -128 + 64 + 32 + 16 + 8 + 2 + 1
= -5

now 
XOR -> SUM WITHOUT CARRY
AND -> CARRY

while (carry){
    carry = (a & b) << 1 (carry is for next bit)
    a = a ^ b
    b = carry
}
return a

Now this algorithm assumes fixed number of bits (as carry is discarted after fixed number of bits are crossed)

Python has no edge. carry never dies for negatives.
fake a 32 bit machine in python
MASK = 0xffffffff = 11111111111111111111111111111111
f = 1111

a = a & MASK (pretend Python is only 32-bit)

MAX = 0x7fffffff = 01111111111111111111111111111111 (Largest positive signed 32-bit integer)

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK    = 0xffffffff
        MAX     = 0x7fffffff
        while b:
            carry = (a&b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
            
        # we do not know if a is positive or not in python
        # in normal 32 bit machine it would have know
        if a > MAX:
            # A is negative 
            # suppose a = 11111111111111111111111111111011
            # python sees just a big + number 
            # ~x = -(x+1)
            return ~(a ^ MASK)
        else:
            return a
