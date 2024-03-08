<<<<<<< HEAD
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and ans[i]==0:
                if temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
                else:
                    ans[i]=stack[-1]-i
            
            stack.append(i) 

        return ans
=======
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and ans[i]==0:
                if temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
                else:
                    ans[i]=stack[-1]-i
            
            stack.append(i) 

        return ans
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
