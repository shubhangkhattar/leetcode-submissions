class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        param_dict = {'(':')','{':'}', '[':']'}
        
        for i in range(len(s)):
            if s[i] in param_dict.keys():
                my_stack.append(s[i])
            elif not my_stack:
                return False
            else:
                ele = my_stack.pop()
                if not param_dict[ele] == s[i]:
                    return False
        
        return False if my_stack else True