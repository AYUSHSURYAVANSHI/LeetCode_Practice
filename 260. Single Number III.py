class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        l = []
        for n, o in nums.items():
            if o == 1:
                l.append(n)
        return l
