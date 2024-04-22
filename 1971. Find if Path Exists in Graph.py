class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        l = defaultdict(list)

        for i, j in edges:
            l[i].append(j)
            l[j].append(i)

        s = set()
        def dfs(node):
            if node == destination:
                return True
            s.add(node)
            for j in l[node]:
                if j not in s and dfs(j):
                    return True
            return False
        
        return dfs(source)