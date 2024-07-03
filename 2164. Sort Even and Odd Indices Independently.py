class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        l1 = sorted([i for j, i in enumerate(nums) if j % 2 == 0])
        l2 = sorted([i for j, i in enumerate(nums) if j % 2 == 1], reverse=True)
        res = []
        for i in range(len(l2)):
            res.append(l1[i])
            res.append(l2[i])

        if len(l1) > len(l2): res.append(l1[-1])
        return res
        