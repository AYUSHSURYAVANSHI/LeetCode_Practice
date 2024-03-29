<<<<<<< HEAD
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(len(nums)-1):
=======
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(len(nums)-1):
>>>>>>> 6565d284220dea1aa3de84faf61b1150f2d66938
            if nums[i]==nums[i+1]:   return nums[i]