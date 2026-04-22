class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap,num)
        self.k = k

    def add(self, val: int) -> int:
        print(self.heap)
        heapq.heappush(self.heap,val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]





 
