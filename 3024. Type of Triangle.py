class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n=len(nums)
        c=0
        a=0
        if abs(nums[0]+nums[1])>nums[2] and abs(nums[0]-nums[1])<nums[2]:
            if nums[0]==nums[1] and nums[1]==nums[2]:
                return "equilateral"
            elif nums[0]==nums[1] and nums[1]!=nums[2] or nums[0]==nums[2] and nums[0]!=nums[1] or nums[1]==nums[2] and nums[1]!=nums[0]:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"


                