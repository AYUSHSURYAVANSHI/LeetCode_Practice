class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[nums[0]]
        for num in nums:
            res=bisect_left(ans,num)
            if res==len(ans):
                ans.append(num)
            elif ans[res]>num:
                ans[res]=num
        return len(ans) 