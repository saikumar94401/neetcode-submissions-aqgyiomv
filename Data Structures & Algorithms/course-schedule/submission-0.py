class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses={}
        
        for course,pre_req in prerequisites:
            
            if course in courses:
                courses[course].append(pre_req)
            else:
                courses[course]=[pre_req]
    

        in_degree={course: 0 for course in range(numCourses)}
       
        for course in prerequisites:
            pre_req=course[1]
            in_degree[pre_req]+=1
        print(in_degree)
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
        

        return len(result)==numCourses


        