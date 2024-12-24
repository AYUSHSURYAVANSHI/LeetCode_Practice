class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # function to get diameter of graph given the edges
        def getDiameter(edges):
            # initiate dict to maintain adjacency list
            children=defaultdict(list)
            # fill the adjacency list
            for u,v in edges:
                children[u].append(v)
                children[v].append(u)

            # initiate the diameter value
            diameter=0

            # recursive dfs call to calculate diameter
            def dfs(curr,parent):
                nonlocal diameter

                # maintain two largest depths among the children
                depths=[0,0]

                # for all children who are not the parent
                for child in children[curr]:
                    if child!=parent:
                        # push the depth for that child, making the total number of depths 3
                        heapq.heappush(depths,dfs(child,curr))
                        # remove the smallest depth, thus maintaining larger 2 depths
                        heapq.heappop(depths)

                    # update global diameter using two largest maintained depths
                    if depths[0]+depths[1]>diameter: diameter=depths[0]+depths[1]

                # return the depth for node having this current node as the child
                return 1+depths[1]

            # carry out the dfs
            dfs(0,-1)

            # return the diameter
            return diameter
        
        # get the diameters for both graphs
        d1=getDiameter(edges1)
        d2=getDiameter(edges2)

        # the diameter will be the max of 3 options:
        # the diameter of first graph (for a large first graph)
        # the diameter of second graph (for a large second graph)
        # the diameter formed by joining the centers of the two graphs (sum of individual radii+1)
        return max(d1,d2,1+((d1+1)//2)+((d2+1)//2))