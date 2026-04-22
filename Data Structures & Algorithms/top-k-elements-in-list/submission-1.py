import heapq

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)

        for nums in nums:
            my_map[nums] += 1
        
        heap = []

        for key in my_map.keys():
            heapq.heappush(heap, (my_map[key],key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for val in heap:
            res.append(val[1])
        
        return res