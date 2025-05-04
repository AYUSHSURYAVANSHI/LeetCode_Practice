class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx, n, currcount, l, ans = max(nums), len(nums), 0, 0, 0

        for r in range(n):
            if nums[r]==mx: currcount+=1
            while currcount>=k:
                ans+=n-r
                if nums[l]==mx: currcount-=1
                l+=1
        
        return ans