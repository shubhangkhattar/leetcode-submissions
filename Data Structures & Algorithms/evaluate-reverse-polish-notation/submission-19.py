class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for token in tokens:
            if token == "+":
                val_2 = my_stack.pop()
                val_1 = my_stack.pop()
                my_stack.append(int(val_1 + val_2))
            elif token == "-":
                val_2 = my_stack.pop()
                val_1 = my_stack.pop()
                my_stack.append(int(val_1 - val_2))
            elif token == "/":
                val_2 = my_stack.pop()
                val_1 = my_stack.pop()
                my_stack.append(int(val_1 / val_2))
            elif token == "*":
                val_2 = my_stack.pop()
                val_1 = my_stack.pop()
                my_stack.append(int(val_1 * val_2))
            else:
                my_stack.append(int(token))
        return my_stack[0]
                