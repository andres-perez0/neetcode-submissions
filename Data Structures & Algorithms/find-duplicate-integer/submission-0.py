class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we're given an array of integers (nums)
        # containing n + 1 integers
        # is in the range [1, n] inclusive 

        node1 = node2 = nums[0]
        while True:
            # gets you where the two pointers meet
            node1 = nums[node1]
            node2 = nums[nums[node2]]
            if node1 == node2:
                break

        node2 = nums[0]
        while node1 != node2:
            node1 = nums[node1]
            node2 = nums[node2]

        return node1