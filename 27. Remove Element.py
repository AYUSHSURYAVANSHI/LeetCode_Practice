<<<<<<< HEAD
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
=======
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return len(nums)