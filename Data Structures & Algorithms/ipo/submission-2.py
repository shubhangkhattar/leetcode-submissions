class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        
        minHeap = [(c,p) for c,p in zip(capital,profits)]
        maxHeap = []
        
        heapq.heapify(minHeap)

        for i in range(k):
            while minHeap and minHeap[0][0] <= w:
                heapq.heappush(maxHeap,-1*heapq.heappop(minHeap)[1])

            if maxHeap:
                w += (-1 * heapq.heappop(maxHeap))
            else:
                break

        return w