class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        
        total_area = 0
        curr_area = 0
        l = 0
        r = 1
        diff = 0

        max_height_i = height.index(max(height)) # debugging solution

        while r <= max_height_i:
            if height[l] <= height[r]:
                curr_area += (min(height[l], height[r]) * (r - l - 1)) - diff
                total_area += curr_area
                curr_area = 0
                diff = 0
                l = r
            else:
                diff += height[r]
            r += 1

        r = n - 1
        l = r - 1
        diff = 0

        while max_height_i <= l:
            if height[r] <= height[l]:
                curr_area += (min(height[l], height[r]) * (r - l - 1)) - diff
                total_area += curr_area
                curr_area = 0
                diff = 0
                r = l
            else:
                diff += height[l]
            l -= 1
        return total_area