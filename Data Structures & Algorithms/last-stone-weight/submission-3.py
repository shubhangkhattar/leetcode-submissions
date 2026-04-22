import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        print(heap)
        while len(heap) > 1:
            stone_1 = -heapq.heappop(heap)
            stone_2 = -heapq.heappop(heap)
            if stone_1 == stone_2:
                continue
            heapq.heappush(heap,-abs(stone_2-stone_1))
        
        return  -heap[0] if heap else 0