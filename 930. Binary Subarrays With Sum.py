<<<<<<< HEAD
class Solution:
    def numSubarraysWithSum(self, a: List[int], g: int) -> int:
        result = 0
        z, s = Counter([0]), 0
        for v in a:
            s += v
            result += z[s-g]
            z[s] += 1

=======
class Solution:
    def numSubarraysWithSum(self, a: List[int], g: int) -> int:
        result = 0
        z, s = Counter([0]), 0
        for v in a:
            s += v
            result += z[s-g]
            z[s] += 1

>>>>>>> 6565d284220dea1aa3de84faf61b1150f2d66938
        return result