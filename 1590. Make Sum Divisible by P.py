<<<<<<< HEAD
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalSum = sum(nums)
        rem = totalSum % p

        if rem == 0:
            return 0

        prefixMod = {0: -1}
        prefixSum = 0
        minLength = len(nums)

        for i, num in enumerate(nums):
            prefixSum += num
            currentMod = prefixSum % p
            targetMod = (currentMod - rem + p) % p

            if targetMod in prefixMod:
                minLength = min(minLength, i - prefixMod[targetMod])

            prefixMod[currentMod] = i

=======
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalSum = sum(nums)
        rem = totalSum % p

        if rem == 0:
            return 0

        prefixMod = {0: -1}
        prefixSum = 0
        minLength = len(nums)

        for i, num in enumerate(nums):
            prefixSum += num
            currentMod = prefixSum % p
            targetMod = (currentMod - rem + p) % p

            if targetMod in prefixMod:
                minLength = min(minLength, i - prefixMod[targetMod])

            prefixMod[currentMod] = i

>>>>>>> 7b6ba8e5995f96beee23a68d301843f134e054cf
        return minLength if minLength < len(nums) else -1