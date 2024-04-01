<<<<<<< HEAD
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        result = 0
        minKIndex = -1
        maxKIndex = -1
        culpritIndex = -1

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                culpritIndex = i

            if nums[i] == minK:
                minKIndex = i

            if nums[i] == maxK:
                maxKIndex = i

            smaller = min(minKIndex, maxKIndex)
            temp = smaller - culpritIndex

            result += temp if temp > 0 else 0

=======
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        result = 0
        minKIndex = -1
        maxKIndex = -1
        culpritIndex = -1

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                culpritIndex = i

            if nums[i] == minK:
                minKIndex = i

            if nums[i] == maxK:
                maxKIndex = i

            smaller = min(minKIndex, maxKIndex)
            temp = smaller - culpritIndex

            result += temp if temp > 0 else 0

>>>>>>> 10b2a6e3a579911ea69ba00fe2504f56a3a8b313
        return result