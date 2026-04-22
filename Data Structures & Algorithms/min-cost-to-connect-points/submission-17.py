class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def distance(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x1-x2) + abs(y1-y2)

        adj_matrix = defaultdict(list)
    
        for i in range(n):
            for j in range(i+1,n):
                d = distance(points[i],points[j])
                adj_matrix[i].append((j,d))
                adj_matrix[j].append((i,d))

        visited = set()
        minHeap = [(0,0)]
        total_distance = 0

        while minHeap:
            distance,point = heapq.heappop(minHeap)

            if point in visited:
                continue
            
            visited.add(point)

            total_distance += distance

            if len(visited) == n:
                return total_distance
            
            for neighbor,distance in adj_matrix[point]:
                heapq.heappush(minHeap,(distance,neighbor))

        

                    

