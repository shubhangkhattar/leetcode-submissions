class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == "]":
                curr_string = ""

                while stack[-1] != "[":
                    curr_string = stack.pop() + curr_string
                stack.pop()
                num = ""
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                curr_string *= int(num)
                stack.append(curr_string)
            else:
                stack.append(char)
    
        
        return "".join(stack)
