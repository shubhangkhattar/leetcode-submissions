class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 1 
        number = nums[0]

        for curr in nums[1:]:
            if curr == number:
                count += 1
            elif count == 0:
                number = curr
                count = 1
            else:
                count -= 1

        return number
            
            

        

        
        
