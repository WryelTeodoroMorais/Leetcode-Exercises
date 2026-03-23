class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            at, prox = 2, 3
            i = 4
            while i <= n:
                at, prox = prox, at+prox
                i+=1
            return prox
         