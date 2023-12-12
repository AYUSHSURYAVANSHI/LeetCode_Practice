class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(d) for d in str(int(''.join(map(str,digits)))+ 1)]