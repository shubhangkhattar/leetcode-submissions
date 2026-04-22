class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            for j in range(i+1,N):
                x1,y1 = points[i]
                x2,y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((distance,j))
                adj[j].append((distance,i))
        
        visited = set()
        result = 0

        heap = [(0,0)]

        while heap:

            distance,u = heapq.heappop(heap)

            if u in visited:
                continue

            result += distance
        
            visited.add(u)

            if len(visited) == len(points):
                break

            for distance,v in adj[u]:
                heapq.heappush(heap,(distance,v))

        return result


