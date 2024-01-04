class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums).values()
        ans = 0
        for i in count :
            if i == 1:
                return -1
            else :
                ans += i // 3 + (i%3!=0)
        return ans