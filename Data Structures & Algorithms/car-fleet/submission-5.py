class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       
        stack = [ (p,s) for p,s in zip(position,speed)]
        stack.sort()

        p,s = stack.pop()
        fleet_time = (target - p) / s

        fleet = 1

        while stack:
            p,s = stack.pop()
            time = (target - p) / s
            if time > fleet_time:
                fleet_time = time
                fleet += 1
        
        return fleet