class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        l,product = 0,1

        for r,num in enumerate(nums):
            product *=num
            while product>=k and l<=r:
                product//=nums[l]
                l+=1
            ans+=r-l+1
        return ans