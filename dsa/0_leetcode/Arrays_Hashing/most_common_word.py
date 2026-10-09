from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        for i in "!?',;.":
            paragraph = paragraph.replace(i, " ")
            
        print(paragraph)
            
        words = paragraph.lower().split()
        counts = Counter(words)
        srt = sorted(counts, key=lambda w: -counts[w])
        print(srt)
        i=0
        while srt[i] in banned:
            i +=1 
        return srt[i] 
        
sol = Solution()
sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"])
        