from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            # Find the index of the minimum value in the array
            min_index = nums.index(min(nums))
            # Replace the minimum value with its product with the multiplier
            nums[min_index] *= multiplier
        return nums