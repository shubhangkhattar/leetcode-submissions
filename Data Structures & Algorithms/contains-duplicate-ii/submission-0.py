class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = set()

        i = 0 
        j = 0


        while j < len(nums):
            if nums[j] in my_set:
                return True
            my_set.add(nums[j])
            j += 1
            if abs(i - j) > k:
                my_set.remove(nums[i])
                i += 1
        return False


        # [1,2,3,1]
        #  0 1 2 3