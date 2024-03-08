class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        li=[i for i in c.values()]
        m,res=max(li),0
        for i in li:
            if i==m:
                res+=i
        return res