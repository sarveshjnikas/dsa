"""
let us start from any index. 
we will try to find out for how many subarrays is the given element minimum

so the solution becomes:
    find previous smaller element index say a
    find next smaller element index say b (increasing stack need to be used)
"""
class Solution:
    def sumSubarrayMins(self, arr):
        sum = 0
        n = len(arr)
        next_smaller = [n]*n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                next_smaller[idx] = i
            
            stack.append(i)
            
        prev_smaller = [-1]*n
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                idx = stack.pop()
                prev_smaller[idx] = i
            stack.append(i)
        
        print(prev_smaller, next_smaller)
        for i in range(n):
            left = i - prev_smaller[i]      # number of choices for left endpoint
            right = next_smaller[i] - i     # number of choices for right endpoint
            sum = sum + left*right*arr[i]
            print(sum)
            
        return sum % (10**9 + 7)