class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        lastOnePos = [0] * n
        def up(i, j) -> None:
            while i < j:
                lastOnePos[j-1], lastOnePos[j] = lastOnePos[j], lastOnePos[j-1]
                j -= 1
        for i in range(n):
            for j in range(n):
                if grid[i][n-1-j] == 1:
                    lastOnePos[i] = n-j
                    break
        for i in range(n):
            for j in range(i, n):
                if lastOnePos[j] <= i+1:
                    res += j - i
                    up(i, j)
                    break
            else:
                return -1
        return res

'''
首先，我们需要找到每一行中最右边的1的位置。
然后，我们从上到下遍历每一行，对于每一行，我们需要找到最近的一行，其最右边的1的位置小于等于当前行的索引加1。
如果找到了这样的行，我们就将其与当前行交换，并记录交换次数。如果没有找到这样的行，说明无法满足条件，返回-1。最后返回总的交换次数。

这个算法的正确性是因为我们总是选择最近的一行进行交换，
这样可以保证我们在最少的交换次数内满足条件，并且从需求上来讲我们每次选择的都是需求最迫切的行进行交换。

时间复杂度O(n^2),空间复杂度O(n)
'''
