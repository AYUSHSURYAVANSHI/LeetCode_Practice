class Solution:
    def isPathCrossing(self, path: str) -> bool:
        return len({0,*accumulate(map({'N':10**5,'E':1,'S':-10**5,'W':-1}.get,path))}) <= len(path)
    