class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        lis=[]
        for i in range(0,len(nums)-2,3):
            if nums[i+2]-nums[i]<=k:
                lis.extend([[nums[i],nums[i+1],nums[i+2]]])
        return lis if len(lis)==len(nums)//3 else []