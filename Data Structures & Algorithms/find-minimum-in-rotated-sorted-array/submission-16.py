class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        min_num = float("inf")

        while l <= r:
            m = (l+r) // 2

            # sorted side.
            if nums[l] <= nums[m]:
                  min_num = min(nums[l],min_num)
                  l = m+1
        
            # unsorted side.
            else:
                min_num = min(nums[m],min_num)
                r = m - 1

        return min_num

        


        # [3,4,5,6,1,2]


        # 5