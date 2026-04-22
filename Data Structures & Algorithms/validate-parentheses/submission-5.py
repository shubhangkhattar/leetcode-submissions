class Solution:
    def isValid(self, s: str) -> bool:
        
        my_stack = []
        param_dict = {'(':')','{':'}', '[':']'}

        for bracket in s:
            if bracket in ")}]":
                if not my_stack:
                    return False
                opening_bracket = my_stack.pop()
                if param_dict[opening_bracket] != bracket:
                    return False
            else:
                my_stack.append(bracket)
        
        return len(my_stack) == 0 
