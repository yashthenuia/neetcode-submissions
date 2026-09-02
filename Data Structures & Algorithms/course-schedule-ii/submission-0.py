class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree =[0]*numCourses
        adj =[[] for i in range(numCourses)]
        for src , des in prerequisites:
            indegree[src] +=1
            adj[des].append(src)
        que = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                que.append(i)

        result =[]
        final=0
        while que:
            node = que.popleft()
            result.append(node)
            final +=1
            for nei in adj[node]:
                indegree[nei] -=1
                if indegree[nei]==0:
                    que.append(nei)
        
        if final ==numCourses:
             return result
        return []