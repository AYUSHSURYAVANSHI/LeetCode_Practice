class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        res = (l*(l+1)/2)
        su = sum(nums)
        return int(res - su)