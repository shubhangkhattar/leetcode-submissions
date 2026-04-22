class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)


        for source,destination,time in times:
            adj[source].append((time,destination))

        print(adj)

        minHeap = []
        
        heapq.heappush(minHeap,(0,k))
        
        visited = set()

        final_time = 0

        while minHeap:
            time,origin = heapq.heappop(minHeap)
            if origin in visited:
                continue
            visited.add(origin)
            final_time = time
            for next_time,destination in adj[origin]:
                heapq.heappush(minHeap,(time+next_time,destination))

        return final_time if len(visited) == n else -1
