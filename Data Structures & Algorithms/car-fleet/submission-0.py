class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed = [(p,s) for p,s in zip(position,speed)]
        speed.sort(reverse=True)

        fleet = 1
        prev_time = (target-speed[0][0])/speed[0][1]

        for p,s in speed[1:]:
            curr_time = (target-p)/s
            if curr_time > prev_time:
                fleet += 1
                prev_time = curr_time

        return fleet