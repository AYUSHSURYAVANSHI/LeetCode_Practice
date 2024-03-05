class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        curr = prev =nums[0]
        for num in nums[1:]:
            if num -1 != prev:
                break 
            curr += num
            prev += 1
        while curr in nums:
            curr += 1
        return curr 