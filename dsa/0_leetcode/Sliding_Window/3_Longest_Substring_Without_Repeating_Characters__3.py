class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        best = 0
        left = 0 
        for right, ch in enumerate(string):
            if ch in last: 
                left = last[ch]+1
            last[ch] = right
            curr = right-left+1
            if curr >  best:
                best = curr
        return best

sol = Solution()
print(sol.lengthOfLongestSubstring("abcddd"))
