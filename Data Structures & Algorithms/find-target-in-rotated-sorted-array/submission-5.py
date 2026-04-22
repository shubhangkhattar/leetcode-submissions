class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left sorted sorted
            if nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right side unsorted
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
                
            

            # [5,6,1,2,3,4]
            #      |

            # 2 
                 



