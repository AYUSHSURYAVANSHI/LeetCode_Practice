<<<<<<< HEAD
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapify(pq:=[-x for x in nums])
        score=0
        for i in range(k):
            x=-heappop(pq)
            score+=x
            if x==1:
                score+=k-1-i
                break
            heappush(pq, -((x+2)//3))
        return score
=======
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapify(pq:=[-x for x in nums])
        score=0
        for i in range(k):
            x=-heappop(pq)
            score+=x
            if x==1:
                score+=k-1-i
                break
            heappush(pq, -((x+2)//3))
        return score
>>>>>>> 7b6ba8e5995f96beee23a68d301843f134e054cf
            