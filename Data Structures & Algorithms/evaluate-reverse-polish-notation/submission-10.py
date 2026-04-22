
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-/*"

        for token in tokens:
            if token in operations:
                val_2 = int(stack.pop())
                val_1 = int(stack.pop())
                if token == "*":
                    stack.append(val_1*val_2)
                if token == "/":
                    stack.append(val_1/val_2)
                if token == "+":
                    stack.append(val_1+val_2)
                if token == "-":
                    stack.append(val_1-val_2)
            else:
                stack.append(token)
        return int(stack[-1])