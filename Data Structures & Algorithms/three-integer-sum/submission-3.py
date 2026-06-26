class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list:List[List[int]] = []
        nums = sorted(nums)
        invalid_sets = set()


        # while i < (k-1):
        #     target = -(nums[i] + nums[k]) # num[j]

        #     for j in range(i+1, k-1):
        #         if nums[j] == target:
        #             return_list.append([nums[i], nums[j], nums[k]])

        #     if target < 0:
        #         i += 1
        #     if target > 0:
        #         k -= 1
   
        for i in range(len(nums)):
            j = i + 1 
            k = len(nums) - 1
            while j < k:
                target = nums[i] +nums[j] + nums[k]

                if target == 0 and (nums[i], nums[j], nums[k]) not in invalid_sets:
                    return_list.append([nums[i], nums[j], nums[k]])
                    invalid_sets.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif target > 0:
                    k -= 1
                else: 
                    j += 1
                

        return return_list
