class Solution:
    def countSubarrays(self, v: List[int], k: int) -> int:
        m = {}
        n = len(v)
        a = max(v)
        i = j = 0
        ans = 0
        while j < n:
            m[v[j]] = m.get(v[j], 0) + 1
            while m.get(a, 0) >= k:
                ans += n - j
                m[v[i]] -= 1
                i += 1
            j += 1
        return ans