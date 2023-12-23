<<<<<<< HEAD
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) -1,-1,-1):
          if num[i] in {'1','3','5','7','9'}:
            return num[:i+1]
=======
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) -1,-1,-1):
          if num[i] in {'1','3','5','7','9'}:
            return num[:i+1]
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return ''