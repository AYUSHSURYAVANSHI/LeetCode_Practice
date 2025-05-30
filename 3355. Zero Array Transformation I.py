class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        delta = [0] * (n + 1)

        # Apply range increments using difference array
        for q in queries:
            l, r = q
            delta[l] += 1
            if r + 1 < n:
                delta[r + 1] -= 1

        # Build prefix sum array to get final increment count at each index
        new_delta = [0] * n
        new_delta[0] = delta[0]
        for i in range(1, n):
            new_delta[i] = new_delta[i - 1] + delta[i]

        # Apply the reverse transformation
        for i in range(n):
            reduced = nums[i] - new_delta[i]
            if reduced > 0:
                return False

        return True