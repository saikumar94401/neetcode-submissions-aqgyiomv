class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses={}
        
        for pre_req,course in prerequisites:
            
            if course in courses:
                courses[course].append(pre_req)
            else:
                courses[course]=[pre_req]
    

        in_degree={course: 0 for course in range(numCourses)}
       
        for course in prerequisites:
            pre_req=course[0]
            in_degree[pre_req]+=1
        
        queue=deque()
        for course in in_degree:
            if in_degree[course]==0:
                queue.append(course)
        result=[]
        while queue:
            
            course=queue.popleft()
            result.append(course)
            if course in  courses:
                for pre_req in courses[course]:
                    in_degree[pre_req]-=1
                    if in_degree[pre_req]==0:
                        queue.append(pre_req)
        

        if len(result)==numCourses:
            return result
        else:
            return []