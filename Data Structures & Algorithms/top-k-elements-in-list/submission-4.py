class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = Counter(nums)
        for key,value in freq_map.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]
