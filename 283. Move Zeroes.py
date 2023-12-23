<<<<<<< HEAD
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0

        for j in range(n):
            if (nums[j] != 0):
                nums[i],nums[j] = nums[j],nums[i]
=======
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0

        for j in range(n):
            if (nums[j] != 0):
                nums[i],nums[j] = nums[j],nums[i]
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
                i += 1