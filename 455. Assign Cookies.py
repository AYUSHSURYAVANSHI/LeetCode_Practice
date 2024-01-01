class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(g)-1
        m=len(s)-1
        g=sorted(g)
        s=sorted(s)
        ans=0
        while min(n,m)>=0:
            if g[n]<=s[m]:
                ans+=1
                m-=1
            n-=1
        return ans