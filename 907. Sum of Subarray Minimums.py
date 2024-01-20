class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9 + 7
        stack = []
        result = 0

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result = (result + arr[j] * (i - j) * (j - k)) % modulo

            stack.append(i)

        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result = (result + arr[j] * (len(arr) - j) * (j - k)) % modulo

        return result