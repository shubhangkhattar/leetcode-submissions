class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        element = None

        for num in nums:
            if max_count == 0:
                element = num
                max_count = 1
            elif element == num:
                max_count += 1
            else:
                max_count -= 1
        
        return element