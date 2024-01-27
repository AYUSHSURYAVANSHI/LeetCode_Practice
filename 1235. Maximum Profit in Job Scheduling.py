class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
         # Combine start time, end time, and profit into a single list of tuples
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        # Initialize DP Array
        dp = [(0, 0)]  # (endTime, profit)

        # Iterate and Update DP
        for start, end, prof in jobs:
            # Use bisect_right instead of custom binary search function
            i = bisect_right(dp, (start, float('inf')))
            if dp[i - 1][1] + prof > dp[-1][1]:
                dp.append((end, dp[i - 1][1] + prof))

        # return the result
        return dp[-1][1]