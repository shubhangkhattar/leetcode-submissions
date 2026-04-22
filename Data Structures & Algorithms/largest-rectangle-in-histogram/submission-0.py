class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for i in range(n):
            ans = max(heights[i],ans)
            min_height = heights[i]

            for j in range(i+1,n):
                min_height =  min(min_height,heights[j])
                area = min_height * (j-i+1)
                ans = max(area,ans)

        return ans