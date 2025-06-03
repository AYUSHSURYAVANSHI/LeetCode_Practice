class Solution:
    def isValid(self, s: str) -> bool:
        # open_param = set(["(","[", "{"])
        dictionary = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for i in s:
            if i in dictionary:
                if stack and stack[-1] == dictionary[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True

        #         stack.append(char)
        #     elif stack and char == dictionary[stack[-1]]:
        #         stack.pop()
        #     else:
        #         return False
        # return stack == []   



