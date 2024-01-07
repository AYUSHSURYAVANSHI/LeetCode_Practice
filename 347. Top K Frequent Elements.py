class Solution:
# from collection import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
           return set(nums)
        count = Counter(nums)

        return heapq.nlargest(k,count.keys(),key = count.get)