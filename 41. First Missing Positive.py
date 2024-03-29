<<<<<<< HEAD
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = {}
        maxi = max(nums, default=0)
        for num in nums:
            mp[num] = True
        for i in range(1, maxi):
            if i not in mp:
                return i
=======
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = {}
        maxi = max(nums, default=0)
        for num in nums:
            mp[num] = True
        for i in range(1, maxi):
            if i not in mp:
                return i
>>>>>>> 6565d284220dea1aa3de84faf61b1150f2d66938
        return 1 if maxi < 0 else maxi + 1