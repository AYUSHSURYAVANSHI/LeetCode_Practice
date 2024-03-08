<<<<<<< HEAD
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_nums=sum(nums)
        n=len(nums)
        for i in range(n-1,1,-1):
            sum_of_nums-=nums[i]
            if sum_of_nums>nums[i]:
                return sum_of_nums+nums[i]
=======
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_nums=sum(nums)
        n=len(nums)
        for i in range(n-1,1,-1):
            sum_of_nums-=nums[i]
            if sum_of_nums>nums[i]:
                return sum_of_nums+nums[i]
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return -1        