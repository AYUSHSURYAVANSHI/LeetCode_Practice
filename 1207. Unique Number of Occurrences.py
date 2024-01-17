class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = []
        for i in Counter(arr).values():
            if i in memo:
                return False
            else:
                memo.append(i)
        return True