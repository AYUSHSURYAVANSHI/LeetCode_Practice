class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            if 9 < n < 100 or 999 < n < 10000 or n == 100000:
                res += 1
        
        return res