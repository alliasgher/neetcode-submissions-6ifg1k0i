class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dic  = {}
        visiting = 0

        for course, prereq in prerequisites:
            dic[course] = dic.get(course, [])
            dic[course].append(prereq)

        def dfs(course):
            print("received course: ", course)
            
            if course not in dic:
                return True
            
            prereqs = dic[course]

            for prereq in prereqs:
                print("prereq: ", prereq)
                if prereq == visiting:
                    return False
                
                if dfs(prereq):
                    if prereq in dic:
                        del dic[prereq]
                else:
                    return False

            return True

        for course in range(numCourses):
            visiting = course
            if not dfs(course):
                return False

        return True


        




            
            
            

                
        