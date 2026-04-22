import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []  # RIGHT (stores larger half)
        self.max_heap = []  # LEFT (stores smaller half, negated for max-heap behavior)
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1

        # Always push into max_heap first (negated for max-heap behavior)
        if not self.min_heap or num <= self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps if max_heap is too big
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Balance the heaps if min_heap is too big
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]  # max_heap stores negative values, so negate it
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]  # min_heap stores positive values
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0  # Average of middle two elements
