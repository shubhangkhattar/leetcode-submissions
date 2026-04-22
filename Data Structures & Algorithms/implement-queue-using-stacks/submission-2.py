class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp_stack = []
        while self.stack:
            temp_stack.append(self.stack.pop())
        temp_stack.append(x)
        while temp_stack:
            self.stack.append(temp_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()
        

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return True if not self.stack else False


[3,2,1,0]

0,



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()