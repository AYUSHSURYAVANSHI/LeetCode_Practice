class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()  # unpaired '(' indices
        sb = list(s)

        for i in range(len(s)):
            if sb[i] == '(':
                stack.append(i)  # Record the unpaired '(' index.
            elif sb[i] == ')':
                if not stack:
                    sb[i] = '#'  # Mark the unpaired ')' as '#'.
                else:
                    stack.pop()  # Find a pair!

        # Mark the unpaired '(' as '#'.
        while stack:
            sb[stack.pop()] = '#'

        return ''.join(char for char in sb if char != '#')