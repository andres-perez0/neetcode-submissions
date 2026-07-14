class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        # trival solution is 
        # prev = nums[0]
        # for n in nums:
        #     if n >= prev:
        #         prev = n
        #     else:
        #         return n
        # return prev

        # def condition(l, r, mid, nums):
        #     if nums[r] > nums[mid]:
        #         return 1
        #     else:
        #         return 0

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1

        return nums[l]




