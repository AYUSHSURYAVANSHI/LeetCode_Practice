<<<<<<< HEAD
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = [i for i in range(1,len(nums))]
        base.append(len(nums)-1)
        nums.sort()
=======
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = [i for i in range(1,len(nums))]
        base.append(len(nums)-1)
        nums.sort()
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return nums == base