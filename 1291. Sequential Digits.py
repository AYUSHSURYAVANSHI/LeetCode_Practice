class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque(range(1, 10))
        res = []
        while queue:
            u = queue.popleft()
            if low <= u <= high:
                res.append(u)
            elif high < u:
                continue
                
            last_num = u % 10
            if last_num != 9:
                queue.append(u * 10 + last_num + 1)
                
        return res