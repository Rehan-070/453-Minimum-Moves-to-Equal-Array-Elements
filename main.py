class Solution:
    def minMoves(self, nums: list[int]) -> int:
        
        # if all(i==nums[0] for i in nums):
        #     return 0
        # elif len(nums)==2:
        #     return 1
        # return max(nums)

        return sum(nums)-len(nums)*min(nums)
