class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        my_set = set()
        total = sum(nums)
        
        if total % 2:
            return False
        
        target = total // 2

        for num in nums:
            set_copy = my_set.copy()
            for num1 in set_copy:
                my_set.add(num1+num)

            my_set.add(num)

            if target in my_set:
                return True

        return False