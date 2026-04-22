class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums) - 1

        while left<right:
            inner_sum = nums[left] + nums[right]

            if inner_sum == target:
                return [left+1,right+1]
            elif inner_sum < target:
                left += 1
            else:
                right -= 1
        


