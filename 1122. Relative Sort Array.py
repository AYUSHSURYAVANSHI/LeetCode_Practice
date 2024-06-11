class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a = 0
        # Step 1: Relative Ordering
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr1[a], arr1[j] = arr1[j], arr1[a]
                    a += 1
        # Step 2: Sorting Remaining Elements
        arr1[a:] = sorted(arr1[a:])
        return arr1