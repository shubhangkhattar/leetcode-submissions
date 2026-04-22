class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        num_length = len(nums)

        for i in range(num_length):
            nums.append(nums[i])
        return nums
