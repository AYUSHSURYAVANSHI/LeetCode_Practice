class Solution:
    def frequencySort(self, s: str) -> str:
        s1=""
        se=Counter(s)
        res=sorted(se.items(), key=lambda x:x[1])
        for i in range(len(res)-1,-1,-1):
            s1=s1+(res[i][0]*res[i][1])
        return s1