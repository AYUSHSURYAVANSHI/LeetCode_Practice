<<<<<<< HEAD
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target :
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        if j == mid:
            return mid +1 
        else:
=======
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target :
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        if j == mid:
            return mid +1 
        else:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
            return mid