<<<<<<< HEAD
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        z=[]
        for i,j in enumerate(nums):
            z.append((i,j))
        z.sort(key = lambda x:x[1])
        max_width=0
        min_index=float("inf")
        for index,value in z:
            max_width=max(max_width,index-min_index)
            min_index=min(min_index,index)
        return max_width
=======
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        z=[]
        for i,j in enumerate(nums):
            z.append((i,j))
        z.sort(key = lambda x:x[1])
        max_width=0
        min_index=float("inf")
        for index,value in z:
            max_width=max(max_width,index-min_index)
            min_index=min(min_index,index)
        return max_width
>>>>>>> 7b6ba8e5995f96beee23a68d301843f134e054cf
        