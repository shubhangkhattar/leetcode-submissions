class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        second = 0

        for i in range(n):
            temp = last
            last = last + second
            second = temp
        
        return last