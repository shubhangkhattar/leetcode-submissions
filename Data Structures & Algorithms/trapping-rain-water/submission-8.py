class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        left = 0
        right = len(height) - 1

        result = 0

        while left <= right:
            leftmax = max(leftmax,height[left])
            rightmax = max(rightmax,height[right])
            
            if leftmax <= rightmax:
                result += max(leftmax-height[left],0)
                left += 1
            else:
                result += max(rightmax-height[right],0)
                right -= 1
            
        return result

#                   i         
#                           j
#         height=[4,2,0,3,2,5]
#                 0 2 4 1 2 0
#         ans = 9

#         height=[4,2,0,3,2,5]
#                 0 2 4 1 2 0

# lm = 3
# rm = 3
#                i 
#                j
# [0,2,0,3,1,0,1,3,2,1]
# 0  0 2 0 2 3 2       
#                  0  0
                   