import heapq
class MinStack:

    def __init__(self):
        self.heap = []
        self.stack = []

    def push(self, val: int) -> None:
        heapq.heappush(self.heap,val)
        self.stack.append(val)

    def pop(self) -> None:
        self.heap.remove(self.stack.pop())
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]
        