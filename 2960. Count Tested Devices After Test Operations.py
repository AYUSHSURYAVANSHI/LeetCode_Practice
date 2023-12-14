class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        s = 0
        for b in batteryPercentages:
            if b > s:
                s += 1
        return s 