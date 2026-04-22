class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left_prefix = [0] * n
        right_prefix = [0] * n

        left_max = 0
        right_max = 0

        for i in range(n):
            
            left_max = max(left_max,height[i])
            left_prefix[i] = abs(left_max - height[i])

            right_max = max(right_max,height[n-i-1])
            right_prefix[n-i-1] = abs(right_max - height[n-i-1])
        
        result = [0] * n

        for i in range(n):
            result[i] = min(left_prefix[i],right_prefix[i])

        return sum(result)