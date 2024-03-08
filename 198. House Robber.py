<<<<<<< HEAD
class Solution:
    def rob(self, nums: List[int]) -> int:
=======
class Solution:
    def rob(self, nums: List[int]) -> int:
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return reduce(lambda a, x: (a[1], max(a[1], a[0] + x)), nums, (0, 0))[1]