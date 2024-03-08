<<<<<<< HEAD
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        res = (l*(l+1)/2)
        su = sum(nums)
=======
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        res = (l*(l+1)/2)
        su = sum(nums)
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return int(res - su)