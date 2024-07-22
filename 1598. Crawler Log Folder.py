<<<<<<< HEAD
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        paths_stack: list[str] = []

        for log in logs:
            if log == "../":
                if paths_stack:
                    paths_stack.pop()
            elif log != "./":
                paths_stack.append(log)

=======
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        paths_stack: list[str] = []

        for log in logs:
            if log == "../":
                if paths_stack:
                    paths_stack.pop()
            elif log != "./":
                paths_stack.append(log)

>>>>>>> b3467e64c7467582cda42326c1bb2f9cec23f9a3
        return len(paths_stack)