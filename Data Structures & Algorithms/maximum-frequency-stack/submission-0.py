class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = {}
        

    def push(self, val: int) -> None:
        valCount = self.count.get(val,0) + 1
        self.count[val] = valCount
        if valCount > self.max_count:
            self.max_count = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_count].pop()
        self.count[val] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()