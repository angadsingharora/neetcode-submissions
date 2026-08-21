class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxx = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxx = max(maxx, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxx = max(maxx, h * (len(heights)-i))
        return maxx