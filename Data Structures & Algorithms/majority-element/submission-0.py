class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 1 
        number = nums[0]
        max_count = 1
        max_number = nums[0]

        for curr in nums[1:]:
            if curr == number:
                count += 1
                if count > max_count:
                    max_count = count
                    max_number = curr
            else:
                count -= 1
                if count == 0:
                    number = curr
                    max_count = 1

        
        return max_number
            
            

        

        
        
