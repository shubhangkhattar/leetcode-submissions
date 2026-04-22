class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        my_set = set()

        for num in nums:
            my_set.add(num)

        for num in nums:
            if num-1 in my_set:
                continue
            count = 0
            while num in my_set:
                count += 1
                num = num+1
            res = max(res,count)

        return res
