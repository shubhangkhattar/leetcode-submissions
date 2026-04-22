import heapq
from math import sqrt,pow 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x1,y1 in points:

            distance =  -abs(sqrt(pow((x1 - 0),2) + pow((y1 - 0),2)))
            heapq.heappush(heap,(distance,[x1,y1]))
            if len(heap) > k:
                heapq.heappop(heap)
    
        return [point[1] for point in heap]
