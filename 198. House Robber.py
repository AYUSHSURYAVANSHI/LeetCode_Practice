class Solution:
    def rob(self, nums: List[int]) -> int:
        return reduce(lambda a, x: (a[1], max(a[1], a[0] + x)), nums, (0, 0))[1]