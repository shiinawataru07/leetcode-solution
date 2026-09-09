class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        freshCnt = 0
        gridCopy = [[val for val in grid[i]] for i in range(m)]
        time = 0
        def valid(x, y) -> bool:
            return 0 <= x and x < m and 0 <= y and y < n and gridCopy[x][y] == 1
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCnt += 1
        while freshCnt > 0:
            changed = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        for idx in range(4):
                            if valid(i + dx[idx], j + dy[idx]):
                                gridCopy[i + dx[idx]][j + dy[idx]] = 2
                                freshCnt -= 1
                                changed = True
            if not changed:
                return -1
            for i in range(m):
                for j in range(n):
                    grid[i][j] = gridCopy[i][j]
            time += 1
        return time


'''
本实现为暴力模拟
时间复杂度O(m^2 n^2) 空间复杂度O(mn)
更好的做法是多源 BFS

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1  # 统计新鲜橘子个数
                elif x == 2:
                    q.append((i, j))  # 一开始就腐烂的橘子

        ans = 0
        while q and fresh:
            ans += 1  # 经过一分钟
            tmp = q
            q = []
            for x, y in tmp:  # 已经腐烂的橘子
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):  # 四方向
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:  # 新鲜橘子
                        fresh -= 1
                        grid[i][j] = 2  # 变成腐烂橘子
                        q.append((i, j))

        return -1 if fresh else ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/rotting-oranges/solutions/2773461/duo-yuan-bfsfu-ti-dan-pythonjavacgojsrus-yfmh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

时间复杂度O(mn) 空间复杂度O(mn)
'''
