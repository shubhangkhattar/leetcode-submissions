class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        
        for i in range(len(nums)):
            num = nums[i]
            count = 1
            while num-1 in my_set:
                num -= 1
                count += 1
            longest = max(longest,count)
                
        return longest

        # nums=[0,3,2,5,4,6,1,1]

        


        # [2,20,4,10,3,4,5]