class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [1] * n
        _hash = defaultdict(int)

        for i in range(n - 1, -1, -1):
            letter = s[i]
            dp[i] = 1 + _hash[letter]

            for j in range(1, k + 1):
                x = chr(ord(letter) + j)
                y = chr(ord(letter) - j)

                if x in _hash:
                    dp[i] = max(dp[i], 1 + _hash[x])
                if y in _hash:
                    dp[i] = max(dp[i], 1 + _hash[y])
            _hash[letter] = dp[i]

        return max(dp)