from math import sqrt,pow
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x1,y1 in points:
            distance = sqrt( pow((x1 - 0),2) + pow((y1 - 0),2))
            heapq.heappush(heap,(-distance,[x1,y1]))
            print((distance,[x1,y1]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for distance,point in heap]
