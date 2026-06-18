class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list, suffix_list = [], []
        n = len(nums)

        for i in range(n):
            prefix_list.append(1)
            if i == 0: 
                continue
            prefix_list[i] = nums[i-1] * prefix_list[i-1]

        for j in range(1,(n+1)):
            if j == 1:
                suffix_list.append(1)
                continue
            
            suffix_list.insert(-j+1,suffix_list[-j+1])
            suffix_list[-j] = nums[-j+1] * suffix_list[-j]

        return [x*y for x, y in zip(prefix_list, suffix_list)]