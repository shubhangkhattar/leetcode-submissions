class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count_1 = 0
        count_2 = 0
        val_1 = None
        val_2 = None

        for num in nums:
            if num == val_1:
                count_1 += 1
            elif num == val_2:
                count_2 += 1
            elif count_1 == 0:
                val_1 = num
                count_1 += 1
            elif count_2 == 0:
                val_2 = num
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1

        count_1 = 0
        count_2 = 0

        result = []

        for num in nums:
            if num == val_1:
                count_1 += 1
            if num == val_2:
                count_2 += 1
        
        k = len(nums) // 3

        if count_1 > k:
            result.append(val_1)
        
        if count_2 > k:
            result.append(val_2)
        
        return result


