class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}

        for course,pre_req in prerequisites:
            adj[course].append(pre_req)
        finished = []
        def canFinish(course,path):
            if course in path:
                return False
            
            if course in finished:
                return True
            
            path.add(course)

            for pre_req in adj[course]:
                if not canFinish(pre_req,path):
                    return False
            adj[course] = []
            finished.append(course)
            path.remove(course)
            return True

        for course in range(numCourses):
            if course not in finished:
                if not canFinish(course,set()):
                    return []

        return finished
