<<<<<<< HEAD
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xorr = nums[0]
        max_xor = (1 << maximumBit) - 1
        
        for i in range(1, n):
            xorr ^= nums[i]
        
        ans = []
        for i in range(n):
            ans.append(xorr ^ max_xor)
            xorr ^= nums[n - 1 - i]
        
=======
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xorr = nums[0]
        max_xor = (1 << maximumBit) - 1
        
        for i in range(1, n):
            xorr ^= nums[i]
        
        ans = []
        for i in range(n):
            ans.append(xorr ^ max_xor)
            xorr ^= nums[n - 1 - i]
        
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return ans