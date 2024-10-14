<<<<<<< HEAD
class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
=======
class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
>>>>>>> 7b6ba8e5995f96beee23a68d301843f134e054cf
        return (ans + 1) // 2