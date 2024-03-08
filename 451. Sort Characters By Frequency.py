<<<<<<< HEAD
class Solution:
    def frequencySort(self, s: str) -> str:
        s1=""
        se=Counter(s)
        res=sorted(se.items(), key=lambda x:x[1])
        for i in range(len(res)-1,-1,-1):
            s1=s1+(res[i][0]*res[i][1])
=======
class Solution:
    def frequencySort(self, s: str) -> str:
        s1=""
        se=Counter(s)
        res=sorted(se.items(), key=lambda x:x[1])
        for i in range(len(res)-1,-1,-1):
            s1=s1+(res[i][0]*res[i][1])
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return s1