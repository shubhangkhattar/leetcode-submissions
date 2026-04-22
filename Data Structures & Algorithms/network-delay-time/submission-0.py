class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import collections, heapq

        visit = set()
        weights = [float("INF") for i in range(n + 1)]  
        time = 0

        my_map = collections.defaultdict(list)
        min_heap = [(0, k)]

        for u, v, w in times:
            my_map[u].append((v, w))

        while min_heap:
            weight, element = heapq.heappop(min_heap)
            if element in visit:
                continue
            visit.add(element)
            time = max(time, weight)
            for v, w in my_map[element]:
                if v not in visit:
                    heapq.heappush(min_heap, (weight + w, v))
        return time if len(visit) == n else -1
