from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # i did
        last_index = {}
        for idx, letter in enumerate(s):
            last_index[letter] = max(last_index[letter], idx) if letter in last_index else idx
            
        # better way to do it:
        # last_index = {letter: idx for idx, letter in enumerate(s)}
        
        partitions = []
        
        start = 0
        while start < len(s):
            max_idx = last_index[s[start]]
            i= start
            while i <= max_idx:
                max_idx = max(max_idx, last_index[s[i]])
                i +=1                
                
            partitions.append(max_idx+1 - start)
            start =  max_idx+1
        return partitions
    
sol = Solution()
sol.partitionLabels(s = "qiejxqfnqceocmy") # [13,1,1]