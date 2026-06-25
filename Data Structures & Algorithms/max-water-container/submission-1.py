class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = (r - l) * min(heights[r], heights[l])
        while l != r:
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            maxArea = max(maxArea, (r - l) * min(heights[r], heights[l]))
        return maxArea
