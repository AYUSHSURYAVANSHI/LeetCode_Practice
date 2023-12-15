class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        i , j = map(set , zip(*paths))
        return next(iter(j - i))