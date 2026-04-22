class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):

            left = i
            right = i

            while left > 0 and heights[left-1] >= heights[i]:
                left -= 1
            while right < len(heights) - 1 and heights[right+1] >= heights[i]:
                right += 1

            area = (right - left + 1) * heights[i]
            max_area = max(max_area, area)
        
        return max_area

