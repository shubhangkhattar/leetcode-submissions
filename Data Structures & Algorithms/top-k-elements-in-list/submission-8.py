class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = Counter(nums)
              
        max_freq = max(freq_map.values())

        buckets = [[] for _ in range(max_freq+1)]
        for key,value in freq_map.items():
            buckets[value].append(key)
        
        result = []
        for bucket in buckets[::-1]:
            result.extend(bucket)
            if len(result) >= k:
                break            

        return result
