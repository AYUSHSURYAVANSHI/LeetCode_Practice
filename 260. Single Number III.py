<<<<<<< HEAD
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        l = []
        for n, o in nums.items():
            if o == 1:
                l.append(n)
        return l
=======
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        l = []
        for n, o in nums.items():
            if o == 1:
                l.append(n)
        return l
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
