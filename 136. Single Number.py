<<<<<<< HEAD
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            n ^= i
=======
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            n ^= i
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return n