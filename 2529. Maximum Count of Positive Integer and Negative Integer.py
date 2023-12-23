<<<<<<< HEAD
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for i in nums:
            if i < 0:
                neg += 1
            elif i> 0:
                pos += 1
        return max(pos,neg)

=======
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for i in nums:
            if i < 0:
                neg += 1
            elif i> 0:
                pos += 1
        return max(pos,neg)

>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
    