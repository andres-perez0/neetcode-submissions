class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        n = 0

        for i, h in enumerate(heights):
            n = i       
            curr_index = [i, h]
            while stk and h <= stk[-1][1]:
                prev = stk.pop()     
            
                curr_area = prev[1] * (n - prev[0])
                # print(f"total_area {prev[1]} * ({n - prev[0]}): {curr_area}")
                if curr_area > max_area:
                    max_area = curr_area

                curr_index[0] = prev[0]

            stk.append(curr_index)
        n += 1 
        while stk: # pops the stk at the end 
            pair = stk.pop()
            width = n - pair[0] # length - current index = width of rectangle
            curr_max = width * pair[1] # w x h
            
            if curr_max > max_area:
                max_area = curr_max

        return max_area

