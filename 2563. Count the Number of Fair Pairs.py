<<<<<<< HEAD
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, v, lower, upper):
        v.sort()
        ans = 0
        for i in range(len(v) - 1):
            low = bisect_left(v, lower - v[i], i + 1)
            up = bisect_right(v, upper - v[i], i + 1)
            ans += up - low
=======
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, v, lower, upper):
        v.sort()
        ans = 0
        for i in range(len(v) - 1):
            low = bisect_left(v, lower - v[i], i + 1)
            up = bisect_right(v, upper - v[i], i + 1)
            ans += up - low
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return ans