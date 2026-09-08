class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def delIsland(x, y) -> None:
            if 0 <= x and x < m and 0 <= y and y < n and grid[x][y] == '1':
                grid[x][y] = '0'
                delIsland(x-1, y)
                delIsland(x, y-1)
                delIsland(x+1, y)
                delIsland(x, y+1)
        cnt = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    cnt += 1
                    delIsland(x, y)
        return cnt



'''
使用 dfs 或 bfs 搜索去除岛屿即可
时间复杂度O(mn)
也可以使用并查集
'''
