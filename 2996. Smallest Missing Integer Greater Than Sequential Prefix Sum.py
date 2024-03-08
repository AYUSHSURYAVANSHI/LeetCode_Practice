<<<<<<< HEAD
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
=======
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
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return curr 