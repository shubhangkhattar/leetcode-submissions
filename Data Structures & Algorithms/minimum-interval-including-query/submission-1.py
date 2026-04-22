class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        result = []
        for query in queries:
            
            heap = []

            for left,right in intervals:
                if left > query:
                    break
                if query <= right:
                    heapq.heappush(heap,right-left+1)
            
            if heap:
                result.append(heapq.heappop(heap))
            else:
                result.append(-1)

        return result