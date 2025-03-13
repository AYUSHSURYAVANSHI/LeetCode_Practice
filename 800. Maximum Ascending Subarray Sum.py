class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ans = -1
        cs = 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                cs += nums[i]
            else:
                ans = max(ans, cs + nums[i])
                cs = 0
                ans = max(ans, nums[i])

        if nums[-1] > nums[-2]:
            ans = max(ans, cs + nums[-1])
            ans = max(ans, nums[-1])

        return ans