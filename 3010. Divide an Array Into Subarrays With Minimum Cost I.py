<<<<<<< HEAD
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
=======
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return nums[0] + sum(sorted(nums[1:])[:2])