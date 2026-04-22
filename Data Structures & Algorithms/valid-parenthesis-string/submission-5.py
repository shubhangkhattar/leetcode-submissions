class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_stack = []
        star = []

        for i,char in enumerate(s):
            if char == "(":
                left_stack.append(i)
            elif char == "*":
                star.append(i)

            else:
                if left_stack:
                    left_stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while left_stack:
            if star and left_stack[-1] < star[-1]:
                left_stack.pop()
                star.pop()
            else:
                return False

        return True





# ( ( * * )
# 0 1 2 3 4


# LEFT  = [ 0 1 
# STAR  = [ 2 3 