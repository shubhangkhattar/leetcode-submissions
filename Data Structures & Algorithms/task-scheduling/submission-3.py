class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        maxHeap = [-1*count for count in counts.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while q or maxHeap:
            time += 1
            
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt,time+n))
            
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(maxHeap,cnt)
            
        return time        