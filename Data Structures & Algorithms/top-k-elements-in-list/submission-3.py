import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}

        for num in nums:
            my_map[num] = my_map.get(num,0) + 1

        
        heap = []

        for key,value in my_map.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]