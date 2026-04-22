class Solution:
    def isValid(self, s: str) -> bool:
        
        para = {")":"(","}":"{","]":"["}
        
        stack = []

        for bracket in s:
            if bracket in "[{(":
                stack.append(bracket)
            elif not stack or stack[-1] != para[bracket]:
                return False
            else:
                stack.pop()
                
        return not stack