class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0 or n == 1:
            return 0

        l = 0 
        r = n - 1
        max_area = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(curr_area, max_area)
            print(max_area)

        return max_area