from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        heap = []

        for num,count in count_dict.items():
            heapq.heappush(heap,(count,num))
                
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]

