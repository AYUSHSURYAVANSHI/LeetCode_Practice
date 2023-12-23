<<<<<<< HEAD
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n = int(num1)
        n1 = int(num2)
        n2 = n+n1
=======
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n = int(num1)
        n1 = int(num2)
        n2 = n+n1
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return str(n2)