class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = [0]

        for operation in operations:
            if operation == "C":
                my_stack.pop()
            elif operation == "D":
                my_stack.append(my_stack[-1]*2)
            elif operation == "+":
                my_stack.append(my_stack[-1]+my_stack[-2])
            else:
                my_stack.append(int(operation))
        
        return sum(my_stack)