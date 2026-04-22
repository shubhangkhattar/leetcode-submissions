from math import ceil,floor
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        min_ans = max(piles)
        while left <= right:
            curr_speed = left + (right-left) // 2
            time = 0
            for pile in piles:
                time += ceil(pile/curr_speed)
                # if curr_speed == 23:
                #     print(pile,":",ceil(pile/curr_speed) )
            if time <= h:
                min_ans = min(min_ans,curr_speed)
                right = curr_speed - 1
            else:
                left = curr_speed + 1

        return min_ans

            

            


