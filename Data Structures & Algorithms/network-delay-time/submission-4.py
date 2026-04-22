class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        
        for source,destination,time in times:
            adj[source].append((destination,time))

        minHeap = [(0,k)]
        visited = set()
        time = 0

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            
            time = w1

            visited.add(n1)

            if len(visited) == n:
                break

            
            for n2,w2 in adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap,(w2+w1,n2))

        return time if len(visited) == n else -1