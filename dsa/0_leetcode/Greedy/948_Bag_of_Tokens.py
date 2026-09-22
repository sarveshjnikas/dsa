from collections import deque
class Solution:
    def bagOfTokensScoreBack(self, tokens: list[int], power: int) -> int:
        # UP if power >= token[i] gain 1        lose token[i] 
        # DO if score >= 1        gain token[i] lose 1
        # AT ANY POINT IF PLAYING EITHER UP OF LOWEST OF DOWN OF BIGGEST
        score = 0
        tokens.sort()    
        def backtrack(toks, pr, scr):
            nonlocal score
            # print(toks, pr, scr)
            if len(toks) == 0 or scr <0 or (len(toks)==1 and toks[0]>pr) :
                # print("im",toks, pr, scr)
                return scr
            
            # CHOOSE UP
            a, b = 0, 0
            if pr >= toks[0]:
                a = backtrack(toks[1:].copy(), pr-toks[0], scr+1)
            
            # print("--")
            
            # CHOOSE DOWN
            if scr>=1:    
                b = backtrack(toks[:-1].copy(), pr+toks[-1], scr-1)
            
            score = max(score, a, b)
            return max(a,b)
            
            
        backtrack(tokens, power, score)
        return score
    
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens)-1
        ms = 0
        score = 0
        while l <= r:
            # print(l, r, power)
            if power >= tokens[l]:
                score +=1
                ms = score
                power = power -tokens[l]
                l +=1
            else:
                if score >= 1:
                    ms = score
                    score = score -1
                    power = power + tokens[r]
                    r -= 1
                else:
                    return ms
        return ms
            
     
     
       
        
        
sol = Solution()
sol.bagOfTokensScore([100], power = 50)
