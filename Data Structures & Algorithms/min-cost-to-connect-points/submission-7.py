class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((distance,j))
                adj[j].append((distance,i))

        visit = set()
        res = 0
        minH = [[0,0]] 

        while len(visit) < N:

            d1,n1 = heapq.heappop(minH)
            
            if n1 in visit:
                continue
            
            res += d1
            visit.add(n1)
            for d2,n2 in adj[n1]:
                heapq.heappush(minH,(d2,n2))
            
            
            
        return res
