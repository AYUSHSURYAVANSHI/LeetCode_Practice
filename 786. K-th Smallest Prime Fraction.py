class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        N = len(arr)
        for i in range(N):
            for j in range(i + 1, N):
                heappush(minHeap, (arr[i] / arr[j], (arr[i], arr[j])))
        for _ in range(k):
            a, b = heappop(minHeap)[1]
        return [a, b]