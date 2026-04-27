class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        arr = []
        
        for c,p in zip(capital,profits):
            arr.append((c,p))

        arr.sort(key = lambda x : (x[0],-x[1]))
        print(arr)
        max_heap = []

        for c,p in arr:                
            while c > w:
                if max_heap and k:
                    w += -1 * heapq.heappop(max_heap)
                    k -= 1
                else:
                    return w
            
            heapq.heappush(max_heap,-p)
        
        while k and max_heap:
            w += -1 * heapq.heappop(max_heap)
            k -= 1


        return w









        # capital = 8


        # [(2, 1), (3, 5), (3, 3), (4, 2), (4, 3)]

        # heap = (3,3) (4, 2), (4, 3)


        # k = [2,1] [3,5]
