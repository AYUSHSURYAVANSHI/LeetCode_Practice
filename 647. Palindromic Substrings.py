<<<<<<< HEAD
class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    count+=1
=======
class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    count+=1
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return count