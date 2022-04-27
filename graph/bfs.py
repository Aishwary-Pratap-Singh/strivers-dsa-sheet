from collections import deque
class Solution:
    
    def bfsOfGraph(self, V, adj):
        # code here
        q = deque()
        # print(adj)
        res = []
        vis = [False for i in range(V)]
    
        q.append(0)
        vis[0] = True
        while len(q) != 0:

            curr_node = q.popleft()
            res.append(curr_node)
      
            for nbr in adj[curr_node]:
                if vis[nbr] == False:
                    q.append(nbr)
                    vis[nbr] = True
        return res
        
