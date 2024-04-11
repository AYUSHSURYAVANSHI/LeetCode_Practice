class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l1 , l2 = [] , []
        for num in nums:
            if num%2==0:l1.append(num)
            else:l2.append(num)  
        nums[0: 2*len(l1) : 2] = l1
        nums[1: 2*len(l2) : 2] = l2
        return nums