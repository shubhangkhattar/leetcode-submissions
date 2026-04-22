class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_matrix = defaultdict(list)

        for course,pre_req in prerequisites:
            adj_matrix[course].append(pre_req)
        
        pre = set()

        print(adj_matrix)

        def cycle(course):
                    

            if course in pre:
                return True

            pre.add(course)
            for pre_course in adj_matrix[course]:
                if cycle(pre_course):
                    return True
                
            pre.remove(course)
            return False
        
        for course in range(numCourses):
            if cycle(course):
                return False
        return True


            