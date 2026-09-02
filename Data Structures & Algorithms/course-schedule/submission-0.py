class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegre = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for src, des in prerequisites:
            indegre[src] +=1
            adj[des].append(src)
        q = deque()
        for i in range(numCourses):
            if indegre[i]==0:
                q.append(i)
        finish=0
        while q:
            node =q.popleft()
            finish +=1
            for nei in adj[node]:
                indegre[nei] -=1
                if indegre[nei]==0:
                    q.append(nei)
        return finish==numCourses


            

