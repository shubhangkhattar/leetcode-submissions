class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        l = 1

        result = max(piles)

        def time_taken(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            return time

        result = r

        while l <= r:
            m = l + (r-l) // 2
        
            time = time_taken(m)
            print(time,m)
            if time < h:
                result = min(result,m)
                r = m - 1
            elif time > h:
                l = m + 1
            else:
                result = min(result,m)
                r = m-1

        return result