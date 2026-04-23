class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        res, maxHeap = "",[]

        for count,char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count != 0:
                heapq.heappush(maxHeap,(count,char))

        while maxHeap:
            cnt1, char1 = heapq.heappop(maxHeap)

            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not maxHeap:
                    return res
                cnt2, char2 = heapq.heappop(maxHeap)
                cnt2 += 1
                res += char2
                if cnt2 != 0:
                    heapq.heappush(maxHeap,(cnt2,char2))
                heapq.heappush(maxHeap,(cnt1,char1))

            else:
                res += char1
                cnt1 += 1
                if cnt1 != 0:
                    heapq.heappush(maxHeap,(cnt1,char1))
        
        return res