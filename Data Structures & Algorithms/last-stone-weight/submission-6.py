class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)

        while len(heap) > 1:
            x1 = -heapq.heappop(heap)
            x2 = -heapq.heappop(heap)
            if x1 == x2:
                continue
            heapq.heappush(heap,-(x1-x2))
        return 0 if not heap else -heap[0]

