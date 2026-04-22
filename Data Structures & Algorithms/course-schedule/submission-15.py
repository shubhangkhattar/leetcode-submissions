class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)
        pre_list = set()
        def detect_course_cycle(course,previous):
            
            nonlocal pre_list

            if course in pre_list:
                return True
            
            pre_list.add(course)
            
            for pre in adj[course]:
                if detect_course_cycle(pre,course):
                    return True
            
            pre_list.remove(course)


            return False

        for i in range(numCourses):
            if detect_course_cycle(i,-1):
                return False
        return True
            