class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        mydict = {}
        for i in range(n):
            mydict[i] = []

        for i, nei in edges:
            mydict[i].append(nei)
            mydict[nei].append(i)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for prereq in mydict[node]:
                if prereq == prev:
                    continue
                if not dfs(prereq, node):
                    return False
                

            return True
            
            
        
        res = dfs(0, -1)
        print(visited)
        return res and (len(visited) == n)

        
        
        