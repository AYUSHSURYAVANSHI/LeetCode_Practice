class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        while s:
            k = 1
            while {*s[:k]}&{*s[k:]}:
                k += 1
            res.append(k)
            s = s[k:]

        return res