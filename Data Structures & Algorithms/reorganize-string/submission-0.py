class Solution:
    def reorganizeString(self, s: str) -> str:
        
        myMap = Counter(s)
        myHeap = [[-cnt,char] for char,cnt in myMap.items()]
        heapq.heapify(myHeap)
        
        res = ""
        prev = None

        while myHeap or prev:
            
            if not myHeap and prev:
                return ""

            cnt,char = heapq.heappop(myHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(myHeap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt,char]

        return res
        



