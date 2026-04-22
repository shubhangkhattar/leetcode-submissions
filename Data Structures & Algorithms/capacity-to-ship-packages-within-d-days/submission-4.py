class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def days_taken(max_weight):
            time = 0
            remaining = 0
            for weight in weights:
                if remaining - weight < 0:
                    time += 1
                    remaining = max_weight
                remaining -= weight
            return time
        result = r
        while l <= r:
            m = l + (r-l) // 2
            time = days_taken(m)
            
            if time > days:
                l = m + 1
            else:
                result = m
                r = m - 1
        
        return result
    