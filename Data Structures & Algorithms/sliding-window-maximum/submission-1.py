class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]

        for r in range(k,len(nums)+1):
            l = r - k
            window = nums[l:r]
            result.append(max(window))

        return result
            


            
