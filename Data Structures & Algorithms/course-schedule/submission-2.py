class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dic  = {}
        visiting = set()

        for course, prereq in prerequisites:
            dic[course] = dic.get(course, [])
            dic[course].append(prereq)

        def dfs(course):
            print("received course: ", course)
            
            if course not in dic:
                return True
            
            prereqs = dic[course]
            visiting.add(course)

            for prereq in prereqs:
                print("prereq: ", prereq)
                if prereq in visiting:
                    return False
                
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            if course in dic:
                del dic[course]

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
            