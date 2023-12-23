<<<<<<< HEAD
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num 
            elif num > max2:
                max2 = num 
        
=======
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num 
            elif num > max2:
                max2 = num 
        
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return (max1 - 1) * (max2 - 1)