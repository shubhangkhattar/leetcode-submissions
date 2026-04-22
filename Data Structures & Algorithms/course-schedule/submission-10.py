class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        
        for course,prereq in prerequisites:
            preMap[course].append(prereq)

        def dfs(course,visited):
            if preMap[course] == []:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq,visited):
                    return False

            visited.remove(course)
            # preMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i,set()):
                return False

        return True