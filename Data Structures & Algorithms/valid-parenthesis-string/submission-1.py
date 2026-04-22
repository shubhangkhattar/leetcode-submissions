class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

    
        for i,char in enumerate(s):
            if char == "*":
                star.append(i)
            elif char == "(":
                left.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        


        while left and star:
            if left.pop() > star.pop():
                return False
        
        return not left
