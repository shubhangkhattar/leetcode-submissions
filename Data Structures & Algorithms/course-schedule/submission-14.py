class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        pre_req = set()

        def dfs(course_i):
            if course_i in pre_req:
                return False
            pre_req.add(course_i)
            for pre in pre_map[course_i]:
                    if not dfs(pre):
                        return False
            pre_req.remove(course_i)
            pre_map[course_i] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False

        return True