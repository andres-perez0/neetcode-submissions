class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqTable = {} 

        for val in nums:
            freqTable[val] = freqTable.get(val, 0) + 1
            if freqTable[val] > 1:
                 return True

        return False


