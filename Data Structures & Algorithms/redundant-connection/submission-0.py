class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(len(edges)+1):
            adj[i] = []

        
        def dfs(u,v, visiting):
            if u in visiting:
                return True

            visiting.add(u)

            for nei in adj[u]:
                if nei == v:
                    continue
                if dfs(nei,u, visiting):
                    return True

            return False

            


        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visiting = set()

            if dfs(u,v, visiting):
                return [u,v]

        