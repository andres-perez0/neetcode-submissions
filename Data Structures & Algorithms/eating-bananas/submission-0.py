class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if not piles:
        #     return 0

        # piles.sort() # O(n log n)
        # # Indexs of left and Right
        # n = len(piles) - 1
        # r = n
        # k = n + 1 # we're going to have a global variable k to be able to keep track of the first avaiable (minimum) solution
        # l = 0
        

        # while l <= r:
        #     mid = (r + l) // 2 # calculates mid point
        #     val = piles[mid]   # the value at the point is the bananas per hour (bph)
        #     # time before
        #     hours_before = (l + 1)  # the number of hours that it would take to get to that point
        #                             # for example at 2 bph in [1,2,3,4] it would take 1 hour at 2 bph before getting to 2
        #     time_left = h - hours_before # local variable for the time left
            
        #     curr = mid
        #     while curr <= n:
        #         # curr = 1, still needs 2 and 3
        #         hours_at_step = (piles[curr] + val - 1) // val # round up division formula I found online (a + b - 1) // 2 
        #         print(f"index {curr}. hours at that step: {hours_at_step} ")
        #         time_left -= hours_at_step
        #         print(f"time_left: {time_left}")
        #         curr += 1
        #     print("done")

        #     # prints out the time left
        #     if time_left == 0:
        #         print("k found")
        #         k = val
        #         break
        #     if time_left > 0:
        #         print("k updated")
        #         k = val
        #         r = mid - 1
        #     else:
        #         l = mid + 1 # time_left < 0

        # return k    

        l = 1 
        r = max(piles)
        k = r
        while l <= r:
            time_left = h
            k_i = (l + r) // 2 # k_i = 2

            for p in piles:
                hours_at_step = (p + k_i - 1) // k_i 
                time_left -= hours_at_step

            if time_left >= 0:
                k = k_i
                r = k_i - 1
            else:
                l = k_i + 1

        return k












