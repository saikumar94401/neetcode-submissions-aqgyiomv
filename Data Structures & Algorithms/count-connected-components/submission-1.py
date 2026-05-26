class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors={i:[] for i in range(n)}
        print(neighbors)

        def add_neighbor(edge1,edge2):
            if edge1 in neighbors:
                neighbors[edge1].append(edge2)
            else:
                neighbors[edge1]=[edge2]
        for edge1,edge2 in edges:
            add_neighbor(edge1,edge2)
            add_neighbor(edge2,edge1)
        print(neighbors)
        

        visited=[False]*n

        def bfs(i):
            queue=deque()
            queue.append(i)
            while queue:
                node=queue.popleft()
                print(node)
                for adgacent in neighbors[node]:
                    if not visited[adgacent]:
                        queue.append(adgacent)
                        visited[adgacent]=True
                

        result=0
        for i in neighbors:
            
            if not visited[i]:
                
                result+=1
                visited[i]=True
                bfs(i)
        return result