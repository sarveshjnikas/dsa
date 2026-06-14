from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n
        for i in range(1, n):
            current_rating = ratings[i]
            left_rating = ratings[i-1]
            
            if current_rating > left_rating:
                candies +=1
        
        for i in range(n-2, -1,-1):
            current_rating = ratings[i]
            right_rating = ratings[i+1]
            
            if current_rating > right_rating:
                candies +=1
        return candies