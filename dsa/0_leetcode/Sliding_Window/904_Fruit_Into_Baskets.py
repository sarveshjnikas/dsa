class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # start anywhere. move right. must pick 1 fruit from each tree. 
        # if tree with fruit tha cannot fit in baskets, stop.
        if len(fruits) == 0:
            return 0
        f = 1
        for i in range(len(fruits)):
            b1 = fruits[i]
            b2 = None
            c = 1
            for j in range(i+1, len(fruits)):
                if b2 != None and fruits[j] != b1 and fruits[j] != b2:
                    break
                
                if b2 == None and fruits[j] != b1:
                    b2 = fruits[j]
                c += 1
                f = max(f,c)            
        return f
    
    def totalFruit(self, fruits: list[int]) -> int:
        i = 0
        j = 0
        c = {}
        f_max = 0
        for j in range(len(fruits)):
            cj = fruits[j]
            if cj not in c:
                if len(c)== 2:
                    while len(c) == 2:
                        c[fruits[i]] -= 1
                        if c[fruits[i]] == 0:
                            del c[fruits[i]]
                        i = i+1
                    c[cj] = 1
                else:
                    c[cj] = 1
            else:
                c[cj] += 1
            f_max  = max(f_max, j-i+1)
        return f_max

        
sol = Solution()
sol.totalFruit(fruits = [1,1,1,2,3,2,2])
