import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]

        time = 0 
        
        visit = set()

        while minHeap:
            w1,n1 =  heapq.heappop(minHeap)
            
            if n1 in visit:
                continue
            
            time = w1
            visit.add(n1)

            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2,n2))

        print(visit)
        return time if len(visit) == n else -1



        