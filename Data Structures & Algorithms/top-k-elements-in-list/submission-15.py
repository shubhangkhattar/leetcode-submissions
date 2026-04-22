class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        
        my_map = [[] for i in range(len(nums) + 1)]

        for num,count in counts.items():
            my_map[count].append(num)

        result = []

        for num_list in my_map[::-1]:
            result += num_list
            if len(result) >= k:
                return result

        return result