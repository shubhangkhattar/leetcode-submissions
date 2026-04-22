class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        res = sum(weights)


        while l <= r:
            m = (l+r) // 2

            curr_day = 1
            remaining_weight = m

            for weight in weights:
                if remaining_weight - weight >= 0:
                    remaining_weight -= weight
                else:
                    remaining_weight = m - weight
                    curr_day += 1
            
            if curr_day > days:
                l = m + 1
            else:
                res = m
                r = m - 1
        
        return res

