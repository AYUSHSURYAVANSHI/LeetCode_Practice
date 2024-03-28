class Solution:
    def maxSubarrayLength(self, v: List[int], k: int) -> int:
        n = len(v)
        m = defaultdict(int)
        i, j, ans = 0, 0, 1
        while i < n and j < n:
            m[v[j]] += 1
            while m[v[j]] > k:
                m[v[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans