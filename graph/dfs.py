    # O(V + E)
    def f(self,node,vis,adj,dfs):
        dfs.append(node)
        vis[node] = True
        for i in adj[node]:
            if vis[i] == False:
                self.f(i,vis,adj,dfs)
            
        
        
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        dfs = []
        vis = [False for i in range(V)]
        for i in range(V):
            if vis[i] == False:
                self.f(i,vis,adj,dfs)
        return dfs
