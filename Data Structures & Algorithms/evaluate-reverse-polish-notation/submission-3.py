class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = {"+","-","/","*",}
        
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                val_2 = stack.pop() 
                val_1 = stack.pop() 
                if char == "+":
                    stack.append(val_1 + val_2)
                elif char == "*":
                    stack.append(val_1 * val_2)
                elif char == "-":
                    stack.append(val_1 - val_2)
                elif char == "/":
                    stack.append(int(val_1 / val_2))
                
        return int(stack[0])


     