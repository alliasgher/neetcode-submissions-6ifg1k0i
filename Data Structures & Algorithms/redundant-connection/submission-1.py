class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(len(edges)+1):
            adj[i] = []

        visiting = set()

        
        def dfs(u,v):
            if u in visiting:
                return True

            visiting.add(u)

            for nei in adj[u]:
                if nei == v:
                    continue
                if dfs(nei,u):
                    return True

            return False

            


        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visiting = set()

            if dfs(u,v):
                return [u,v]

        