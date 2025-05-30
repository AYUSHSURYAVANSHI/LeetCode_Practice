class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        start , end = 0 , k-1
        res = float('inf')

        while end < len(nums):
            res = min(res, nums[end] - nums[start])
            start += 1
            end += 1
        return res  