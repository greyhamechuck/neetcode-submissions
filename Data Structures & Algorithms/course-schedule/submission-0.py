class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)] 

        result =0 

        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0) 

        while queue:
            curr = queue.popleft()
            result +=1
            for nxt in graph[curr]:
                indegree[nxt] -=1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return result == numCourses