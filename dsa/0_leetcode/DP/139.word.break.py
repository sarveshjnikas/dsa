from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # SEEMS IT MATTER WHERE WE SPLIT THE FIRST WORD
        wordDict = {wordDict[i]: i for i in range(len(wordDict)) }
        yesDict = {}
        
        def dfs(word):
            if word in wordDict:
                yesDict[word] = True
                return True
            
            a = False
            for i in range(1,len(word)):
                new = word[:i]
                rest = word[i:]
                if new in wordDict:
                    b = yesDict[rest] if rest in yesDict else dfs(rest)
                    a  = a or b
                    if a == True:
                        return True
            yesDict[word] = False
            return a
        return dfs(s)