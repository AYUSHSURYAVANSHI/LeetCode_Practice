class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        if nums.count(1)>0: return False
        mx = max(nums)+1
        sieve = list(range(mx))
        for i in range(4, mx, 2):
            sieve[i] = 2
        for i in range(3, ceil(sqrt(mx))):
            if sieve[i] != i: continue
            for j in range(i * i, mx, i):
                if (sieve[j] == j):
                    sieve[j] = i
        def factorize(num):
            while (num != 1):
                yield sieve[num]
                num = num // sieve[num]
        g = defaultdict(set)
        for num in set(nums):
            for p in factorize(num):
                g[num].add(p)
                g[p].add(num)
        dq,seen = deque([nums[0]]),{nums[0]}
        while dq:
            num = dq.popleft()
            for nxt in g[num]:
                if nxt in seen: continue
                seen.add(nxt)
                dq.append(nxt)
        return len(seen)==len(g)