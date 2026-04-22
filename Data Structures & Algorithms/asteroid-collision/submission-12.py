class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = [asteroids[0]]

        for asteroid in asteroids[1:]:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue

                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break

                if not stack:
                    stack.append(asteroid)
                break
        
            else:
                stack.append(asteroid)
            

        return stack