class MedianFinder:

    def __init__(self):
        self.minHeap = [] #right Heap
        self.maxHeap = [] #left Heap

    def addNum(self, val: int) -> None:

        if self.minHeap and val >= self.minHeap[0]:
            heapq.heappush(self.minHeap,val)
        else:
            heapq.heappush(self.maxHeap,-val)

        leftSize =  len(self.maxHeap)
        rightSize =  len(self.minHeap)
        
        if abs(leftSize - rightSize) > 1:
            if leftSize > rightSize:
                val = -1 * heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap,val)
            else:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap,-val)

    
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            valLeft = self.maxHeap[0] * -1
            valRight = self.minHeap[0]
            return (valLeft + valRight) / 2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]

        

# (Max) LeftHeap  = [-2]
# (Min) RightHeap = [1]
        