class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        maxdepth = 0
        depth = 0
        ans = [0] * len(seq)
        for ch in seq:
            depth += 1 if ch == '(' else -1
            maxdepth = max(maxdepth, depth)
        depth = 0
        for i, ch in enumerate(seq):
            if ch == '(':
                depth += 1
                ans[i] = 1 if depth <= maxdepth // 2 else 0
            else:
                ans[i] = 1 if depth <= maxdepth // 2 else 0
                depth -= 1
        return ans


'''
有效括号字符串（VPS）我发现可以计算每个括号所处的深度，抽象成一个多层级的结构，我们只需要将深度更高的一半的括号分为一组，深度更低的一半的括号分为另一组，这样就可以保证两组括号的嵌套深度的最大值最小。
具体来说，我们可以使用一个计数器来跟踪当前的深度，当遇到左括号时，深度加一，当遇到右括号时，深度减一。  
值得一提的是，我在题解上看到了我这种方法还有更好的优化，就是通过对深度进行奇偶性判断来直接分配组别，这样可以不去计算最大深度，减少计算量。

时间复杂度 O(n) 空间复杂度 O(1)
'''
