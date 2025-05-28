class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = arr[-1] - arr[0]
        nums = []

        for i in range(len(arr) - 1):
            minDiff = min(minDiff,arr[i+1] - arr[i])

        for i in range(len(arr)):
            if (arr[i] - arr[i-1] == minDiff):
                nums.append([arr[i-1], arr[i]])
        return nums