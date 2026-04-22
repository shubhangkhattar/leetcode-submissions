class FreqStack:

    def __init__(self):
        self.valCount = defaultdict(int)
        self.stacks = defaultdict(list)
        self.maxCount = 0
        
    def push(self, val: int) -> None:
        self.valCount[val] += 1
        if self.valCount[val] > self.maxCount:
            self.maxCount = self.valCount[val]
        self.stacks[self.valCount[val]].append(val)


    def pop(self) -> int:
        val = self.stacks[self.maxCount].pop()
        self.valCount[val] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


5,7,5,4,