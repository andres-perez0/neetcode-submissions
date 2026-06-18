class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        return_list = [1 for _ in range(len(nums))]
        print(return_list)

        for i, val in enumerate(nums):

            for j, val_2 in enumerate(return_list):
                if i == j:
                    return_list[j] = val_2
                else:
                    return_list[j] = nums[i] * val_2
    

        return return_list