<<<<<<< HEAD
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
=======
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return ((3*sum((set(nums)))) - sum(nums))//2