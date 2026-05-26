class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            curr = right - left + 1
            if curr > best:
                best = curr
        return best
sol = Solution()
print(sol.lengthOfLongestSubstring("abcddd"))
