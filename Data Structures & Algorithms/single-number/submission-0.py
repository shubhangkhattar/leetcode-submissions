class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = nums[i]
            nums.pop(i)
            if num not in nums:
                return num
            nums.insert(i,num)