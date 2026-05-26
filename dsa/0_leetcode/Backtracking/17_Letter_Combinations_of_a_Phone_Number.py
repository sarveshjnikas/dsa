class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_mapping = {
            2: ["abc"],
            3: ["def"],
            4: ["ghi"],
            5: ["jkl"],
            6: ["mno"],
            7: ["pqrs"],
            8: ["tuv"],
            9: ["wxyz"],
        }
        
        res = []
        def backtrack(s, i):
            if i >= len(digits):
                if len(s) == len(digits):
                    res.append(s)
                return
            
            for letter in letter_mapping[int(digits[i])][0]:
                # choices: add the letter
                backtrack(s+letter, i+1)
                
                # do not add the letter
                backtrack(s, i+1)
            
        backtrack("", 0)
        return res
        
sol = Solution()
sol.letterCombinations(digits = "2")
