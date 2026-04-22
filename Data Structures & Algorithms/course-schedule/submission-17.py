class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}

        for course,pre_req in prerequisites:
            adj[course].append(pre_req)

        def canFinish(course,path):
            if course in path:
                return False
            
            path.add(course)

            for pre_req in adj[course]:
                if not canFinish(pre_req,path):
                    return False

            path.remove(course)
            return True

        for course in range(numCourses):
            if not canFinish(course,set()):
                return False

        return True
