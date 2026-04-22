from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        bucket = [list() for i in range(len(nums) + 1)]

        for num,count in count_dict.items():
            bucket[count].append(num)
        
        result = []


        for nums in bucket[::-1]:
            result += nums
            if len(result) >= k:
                break

        return result