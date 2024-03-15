class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        # Calculate left prefix product
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Calculate right suffix product
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Calculate result array
        result = [left[i] * right[i] for i in range(n)]
       
        return result