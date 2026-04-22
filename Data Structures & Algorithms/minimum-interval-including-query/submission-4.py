class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        query_map = {}
        i = 0
        minHeap = []

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q :
                l,r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r, (l,r)))
                i += 1
            print(minHeap)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            query_map[q] = minHeap[0][0] if minHeap else -1

        return [query_map[q] for q in queries]
            


