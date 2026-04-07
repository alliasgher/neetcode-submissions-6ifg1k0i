class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mydict = {}
        visiting = set()
        visited = set()
        res = []
        for course in range(numCourses):
            mydict[course] = []

        for crs,prereq in prerequisites:
            mydict[crs].append(prereq)

        def dfs(crs):
            if crs in visiting:
                return False

            if crs in visited:
                return True
            
            visiting.add(crs)

            for prereq in mydict[crs]:
                if not dfs(prereq):
                    return False

                
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res
                



        
        