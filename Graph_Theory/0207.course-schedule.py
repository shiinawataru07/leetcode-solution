class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0] * numCourses
        graph = {}
        for pair in prerequisites:
            if pair[0] not in graph:
                graph[pair[0]] = []
            graph[pair[0]].append(pair[1])
        def dfs(node) -> bool:
            color[node] = 1
            if node not in graph:
                color[node] = 2
                return False
            for neighbor in graph[node]:
                if color[neighbor] == 1 or (color[neighbor] == 0 and dfs(neighbor)):
                    return True
            color[node] = 2
            return False
        for node in range(numCourses):
            if color[node] == 0:
                if dfs(node):
                    return False
        return True


'''
dfs 三色标记 检测有向图中是否存在环路问题
时间复杂度O(n+m) 空间复杂度O(n+m) 其中 n 为节点数，m 为边数
'''
