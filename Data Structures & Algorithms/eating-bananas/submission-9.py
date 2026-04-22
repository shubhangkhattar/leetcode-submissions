class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        l = 1
        res = max(piles)
        
        while l <= r:

            m = (l + r) // 2

            time_to_eat = 0

            for pile in piles:
                time_to_eat += math.ceil(pile/m)

            if time_to_eat > h:
                l = m + 1
            else:
                res = m
                r = m -1
        
        print(l,r)
        return res







         
