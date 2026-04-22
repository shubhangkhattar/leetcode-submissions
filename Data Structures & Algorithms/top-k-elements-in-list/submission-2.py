import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}

        for num in nums:
            my_map[num] = my_map.get(num,0) + 1

        
        heap = []

        for key,value in my_map.items():
            heapq.heappush(heap,(-value,key))
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result