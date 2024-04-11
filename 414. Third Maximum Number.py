class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(set(nums))
        l.sort()
        if len(l)>=3:
            return l[len(l)-3]
        return max(l) 