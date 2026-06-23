class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I imagine each element as a circle
        # first, its just [100] 
        # second, its just [100], [4]
        # third, its just [100], [4], [200]
        # fourth, its [100], [4], [200], [1]
        # fifth, its [100], [4], [200], [1], [3] -> [100], [3] -> [4], [200], [1]
        # sixth, its [100], [3] -> [4], [200], [1], [2] 
        ##### == its [100], [2] -> [3] -> [4], [200], [1]
        ##### == its [100], [1] -> [2] -> [3] -> [4], [200]
        # transforms the array into a set to get constant look up time

        if len(nums) <= 0:
            return 0

        global_set_max = 0
        nums = set(nums)
        for n in nums:
            # if there's no n - 1 the current n, there theres no way for it to be consecutive
            if n - 1 not in nums or len(nums) == 1:
                # locally set up the counts
                nn = n
                set_max = 1
                while nn + 1 in nums:                    
                    set_max += 1
                    nn += 1

                if global_set_max < set_max: 
                    global_set_max = set_max

        return global_set_max 