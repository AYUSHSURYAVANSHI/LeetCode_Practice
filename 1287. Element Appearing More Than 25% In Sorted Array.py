class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        p = n // 4

        for i in range(n-p):
            if arr[i] == arr[i+p]:
                return arr[i] 