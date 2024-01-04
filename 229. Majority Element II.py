class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:  
        d = []
        for i in set(nums):
            if nums.count(i)  >  len(nums)/3:
                d.append(i)
        return d
        