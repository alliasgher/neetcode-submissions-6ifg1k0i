class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        mydict = {}
        for i in range(n):
            mydict[i] = []

        for i, nei in edges:
            mydict[i].append(nei)
            mydict[nei].append(i)

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in mydict[node]:
                dfs(nei)

        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count

        

        