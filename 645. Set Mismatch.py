<<<<<<< HEAD
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate=next(i for i in nums if nums.count(i)>1)
        missing=next(i for i in range(1,len(nums)+1) if i not in nums)
=======
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate=next(i for i in nums if nums.count(i)>1)
        missing=next(i for i in range(1,len(nums)+1) if i not in nums)
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return [duplicate, missing]