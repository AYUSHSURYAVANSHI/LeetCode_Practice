class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_num = 0
        for i in s:
            if i == "(":
                count += 1
                if max_num < count:
                    max_num = count
            if i == ")":
                count -= 1
        return(max_num)