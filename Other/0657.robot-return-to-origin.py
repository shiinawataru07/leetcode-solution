class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')

'''
只需要判断左右移动和上下移动是否数量匹配即可
若使用hashmap记录则反而会有不必要的开销
也可以直接记录x和y坐标模拟

class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0

作者：力扣官方题解
链接：https://leetcode.cn/problems/robot-return-to-origin/solutions/389888/ji-qi-ren-neng-fou-fan-hui-yuan-dian-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
