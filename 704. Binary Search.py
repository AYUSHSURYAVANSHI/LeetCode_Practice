<<<<<<< HEAD
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return -1 
=======
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return -1 
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        