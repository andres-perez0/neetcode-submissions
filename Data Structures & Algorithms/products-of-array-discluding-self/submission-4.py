class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # initialized both lists to a fixed size of n filled with 1s
        prefix_list = [1] * n
        suffix_list = [1] * n
        
        for i in range(n):
            if i == 0: 
                continue
            prefix_list[i] = nums[i-1] * prefix_list[i-1]

        print(prefix_list)

        for j in range(n - 2, -1, -1):
            suffix_list[j] = nums[j+1] * suffix_list[j+1]

        return [x*y for x, y in zip(prefix_list, suffix_list)]