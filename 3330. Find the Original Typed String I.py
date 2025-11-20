class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1         # flawless case
        i, n = 0, len(word)

        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1              # walk to block end
            ans += (j - i - 1)      # add (L‑1) extra originals
            i = j                   # jump to next block
        return ans