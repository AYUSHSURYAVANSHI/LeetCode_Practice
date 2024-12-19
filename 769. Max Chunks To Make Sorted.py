class Solution:
    def maxChunksToSorted(self, a: List[int]) -> int:
        return sum(map(eq,accumulate(a,max),count(0)))