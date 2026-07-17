from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # will store indices
        max_area = 0
        
        # Add a sentinel bar of height 0 at the end
        heights.append(0)
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack is empty, width = i
                # Else width = i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area
