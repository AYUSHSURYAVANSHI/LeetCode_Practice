class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1),len(str2)
        if str1 == str2:
            return str1
        if m > n:
            str1,str2 = str2,str1
            n,m = m,n
        if str1.startswith(str2):
            return self.gcdOfStrings(str1[m:],str2)
        return ""