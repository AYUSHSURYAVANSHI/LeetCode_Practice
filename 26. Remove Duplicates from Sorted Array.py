<<<<<<< HEAD
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[l]:
                l += 1
                nums[l] =nums[i]
        return l+1 
=======
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[l]:
                l += 1
                nums[l] =nums[i]
        return l+1 
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        