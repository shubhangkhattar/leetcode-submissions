class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        stack_dict = {"(":")","{":"}","[":"]"}

        for char in s:
            if char in stack_dict:
                my_stack.append(char)
            elif not my_stack or stack_dict[my_stack.pop()] != char:
                return False
        
        return not my_stack