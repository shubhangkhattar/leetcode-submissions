class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack to store indices of bars
        max_area = 0  # Variable to track the maximum area
        
        heights.append(0)  # Append a zero to handle remaining elements in the stack
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area