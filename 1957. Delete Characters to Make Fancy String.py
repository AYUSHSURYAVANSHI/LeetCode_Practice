<<<<<<< HEAD
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                cnt += 1
                if cnt < 3:
                    ans += s[i]
            else:
                cnt = 1
                ans += s[i]
=======
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                cnt += 1
                if cnt < 3:
                    ans += s[i]
            else:
                cnt = 1
                ans += s[i]
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return ans