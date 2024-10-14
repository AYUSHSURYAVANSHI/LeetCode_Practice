<<<<<<< HEAD
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c == "B" and stack[-1] == "A":
                stack.pop()
            elif c == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(c)
=======
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c == "B" and stack[-1] == "A":
                stack.pop()
            elif c == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(c)
>>>>>>> 7b6ba8e5995f96beee23a68d301843f134e054cf
        return len(stack)