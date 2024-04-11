class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for num in nums:
            if num%2==0:
                l1.append(num)
            else:
                l2.append(num)
        return l1 + l2