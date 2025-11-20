import heapq

class Solution:
    def minimumDifference(self, nums):
        n = len(nums)
        k = n // 3
        leftMins = [0] * n
        rightMaxs = [0] * n

        maxLeft = []
        leftSum = 0
        for i in range(k):
            heapq.heappush(maxLeft, -nums[i])
            leftSum += nums[i]
        leftMins[k - 1] = leftSum

        for i in range(k, n - k):
            if nums[i] < -maxLeft[0]:
                leftSum += nums[i] + heapq.heappop(maxLeft)
                heapq.heappush(maxLeft, -nums[i])
            leftMins[i] = leftSum

        minRight = []
        rightSum = 0
        for i in range(n - 1, n - k - 1, -1):
            heapq.heappush(minRight, nums[i])
            rightSum += nums[i]
        rightMaxs[n - k] = rightSum

        for i in range(n - k - 1, k - 2, -1):
            if nums[i] > minRight[0]:
                rightSum += nums[i] - heapq.heappop(minRight)
                heapq.heappush(minRight, nums[i])
            rightMaxs[i] = rightSum

        minDiff = float('inf')
        for i in range(k - 1, n - k):
            minDiff = min(minDiff, leftMins[i] - rightMaxs[i + 1])

        return minDiff