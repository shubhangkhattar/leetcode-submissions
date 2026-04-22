class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        my_list = []

        for i in range(len(nums)):

            if len(my_list) > k:
                my_list.pop(0)

            if nums[i] in my_list:
                return True
            
            my_list.append(nums[i])
        
        return False