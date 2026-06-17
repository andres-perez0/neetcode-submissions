class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for ith, val in enumerate(nums):
            # Set an index-value pair dictionary
            num_dict[ith] = val # {0:5, 1:5}

            if ith == 0: # skip if you're the first (nothing to compare)
                continue

            diff_val = target - val # You're trying to find the value that matches what you want

            if diff_val in num_dict.values(): # if that value is appearnt in your values you have to find the key
                for ind, diff in num_dict.items():
                    if diff == diff_val and ind != ith:
                        return [ind, ith] 
        
        return []