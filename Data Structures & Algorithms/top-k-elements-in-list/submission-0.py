from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)

        for nums in nums:
            my_map[nums] += 1
        
        return sorted(my_map,reverse=True,key=lambda k:my_map[k])[0:k]