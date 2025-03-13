from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, high, count = [], [], 0

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                count += 1
            else:
                high.append(num)

        return less + [pivot] * count + high