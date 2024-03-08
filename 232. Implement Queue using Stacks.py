<<<<<<< HEAD
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)    
        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self) -> int:
        return self.s1.pop()


    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
=======
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)    
        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self) -> int:
        return self.s1.pop()


    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
# param_4 = obj.empty()