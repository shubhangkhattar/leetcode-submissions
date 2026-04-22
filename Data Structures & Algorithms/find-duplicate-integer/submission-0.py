class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for i in range(1,len(nums)+1):
            if i in nums:
                index = nums.index(i)
                nums[index] = -1
        for num in nums:
            if num != -1:
                return num
            