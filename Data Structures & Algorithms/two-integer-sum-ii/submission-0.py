class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0

        while l < r:
            sum_t = numbers[l] + numbers[r]

            if sum_t == target:
                return [l+1, r+1]
            
            if sum_t > target: 
                r -= 1 

            elif sum_t < target:
                l += 1
