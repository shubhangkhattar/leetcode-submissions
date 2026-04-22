from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [(p, s) for p, s in zip(position, speed)]
        stack.sort()
        
        if not stack:
            return 0
        
        p, s = stack.pop()
        time = (target - p) / s
        fleet = 1
        
        while stack:
            p, s = stack.pop()
            time_stack = (target - p) / s
            if time_stack > time:
                fleet += 1
                time = time_stack
        
        return fleet
