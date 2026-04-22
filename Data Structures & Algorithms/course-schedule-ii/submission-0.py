class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(list)

        for course,pre in prerequisites:
            pre_map[course].append(pre)

        pre_req = set()
        completed = []

        def dfs(course_i):
            if course_i in pre_req:
                return False
            
            if course_i in completed:
                return True
            
            pre_req.add(course_i)
            for pre in pre_map[course_i]:
                if pre not in completed:
                   if not dfs(pre):
                    return False

            pre_req.remove(course_i)
            completed.append(course_i)
            return True

        for course_i in range(numCourses):
            dfs(course_i)
        
        return completed if len(completed) == numCourses else []