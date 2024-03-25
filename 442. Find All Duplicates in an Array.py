class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                result.append(num)
            nums[idx] *= -1
        return result