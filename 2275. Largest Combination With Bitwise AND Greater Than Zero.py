<<<<<<< HEAD
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(1 for candidate in candidates if candidate & (1 << i))
            ans = max(ans, cnt)
=======
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(1 for candidate in candidates if candidate & (1 << i))
            ans = max(ans, cnt)
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return ans