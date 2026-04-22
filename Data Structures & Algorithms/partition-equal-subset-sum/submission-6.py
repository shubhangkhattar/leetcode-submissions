class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2

        dp = set()
        dp.add(0)


        for num in nums:
            dp2 = dp.copy()
            
            for num1 in dp2:
                dp.add(num1+num)

            if target in dp:
                return True

        return False