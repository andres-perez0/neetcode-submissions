class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                # if the left side is sorted
                if nums[l] <= target and target < nums[mid]:
                    # this is what we expect in normal binary search
                    r = mid - 1
                else: 
                    # this is to handle if the it's actually on the right side
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    # this is what we expect in normal binary search
                    l = mid + 1
                else:
                    # this is to handle if the number is actually on the left side
                    r = mid - 1   
        return -1