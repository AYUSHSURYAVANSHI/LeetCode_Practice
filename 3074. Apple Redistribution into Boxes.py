class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple.sort()
        capacity.sort(reverse=True)
        j = s1 = s2 = 0
        for i in range(len(apple)):
            s1 += apple[i]
            while s2 < s1:
                s2 += capacity[j]
                j += 1
        
        return j