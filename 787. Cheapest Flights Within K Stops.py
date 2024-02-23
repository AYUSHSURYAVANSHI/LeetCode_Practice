class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for i in range(n)]
        for u,v,d in flights:
            adj[u].append((v,d))
        pq=[(0,src,0)]
        dist=[float('inf')]*n
        dist[src]=0
        heapify(pq)
        stop=0
        while pq:
            stop,node,d=heappop(pq)
            for v,price in adj[node]:
                s=stop
                if dist[v]>price+d:
                    s+=1
                    if s<=k+1:
                        dist[v]=price+d
                        heappush(pq,(s,v,dist[v]))
        if k+1>=stop and dist[dst]!=float('inf'):
            return dist[dst]
        return -1