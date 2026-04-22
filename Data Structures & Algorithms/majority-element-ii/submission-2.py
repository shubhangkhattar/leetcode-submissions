class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1 = 0
        count2 = 0
        num1 = None
        num2 = None

        for num in nums:
            if num1 == num:
                count1 += 1
                continue
            if num2 == num:
                count2 += 1
                continue
            if count1 == 0:
                num1 = num
                count1 += 1
                continue
            if count2 == 0:
                num2 = num
                count2 += 1
                continue
            count1 -= 1
            count2 -= 1

        result = []
        n = len(nums)
        count1 = 0
        count2 = 0
        for num in nums:
            if num1 == num:
                count1 += 1
            if num2 == num:
                count2 += 1

        if count1 > n//3:
            result.append(num1)

        if count2 > n//3:
            result.append(num2)

        return result

        #  |
        # [5,2,3,2,2,2,2,5,5,5]

        # c1 = 1
        # c2 = 5
        # num1 = 1
        # num2 = 2
