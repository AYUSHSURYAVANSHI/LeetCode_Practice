<<<<<<< HEAD
class Solution(object):
    def longestSubarray(self, nums):
        ans, cnt = 0, 0
        
        max_element = max(nums)
        for num in nums:
            if num == max_element:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans
    
=======
class Solution(object):
    def longestSubarray(self, nums):
        ans, cnt = 0, 0
        
        max_element = max(nums)
        for num in nums:
            if num == max_element:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
