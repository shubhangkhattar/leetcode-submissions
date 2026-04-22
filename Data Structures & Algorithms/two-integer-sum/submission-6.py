class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myDict = {}

        for i,num in enumerate(nums):
            if nums[i] in myDict:
                return [myDict[nums[i]],i]
            myDict[target-num] = i