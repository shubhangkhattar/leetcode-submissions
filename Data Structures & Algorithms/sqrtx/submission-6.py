class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            sqr = m * m
            if sqr == x:
                return m
            if sqr > x:
                r = m - 1
            else:
                l = m + 1
        return r