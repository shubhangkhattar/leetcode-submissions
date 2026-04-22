import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        res = high
        while low <= high:
            
            k = low + (high-low) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                res = k
                high = k-1
            else:
                low = k+1
        
        return res



            
