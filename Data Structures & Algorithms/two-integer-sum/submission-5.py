class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myDict = {}

        for i,num in enumerate(nums):
            remainder = target-num
            if remainder in myDict:
                return [myDict[remainder],i]
            
            myDict[num] = i