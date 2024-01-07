class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorted_arr = []

        for x in arr2:
            while x in arr1:
                sorted_arr.append(x)
                arr1.remove(x)
        return (sorted_arr + sorted(arr1))