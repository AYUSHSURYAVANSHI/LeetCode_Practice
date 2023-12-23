<<<<<<< HEAD
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
=======
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return [int(d) for d in str(int(''.join(map(str,digits)))+ 1)]