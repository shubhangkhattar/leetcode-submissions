class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = [asteroids[0]]

        for asteroid in asteroids[1:]:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) >  stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) ==  stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            
            else:
                 stack.append(asteroid)

        return stack


[2,4,-4,-1]

[2,]