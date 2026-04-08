class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k
        cnt = blocks[0 : k].count('B')
        res = cnt
        while right < len(blocks) :
            if blocks[right] == 'B' :
                cnt += 1
            right += 1
            if blocks[left] == 'B' :
                cnt -= 1
            left += 1
            res = max(res, cnt)
        return k - res


'''
解析：
定长滑动窗口
考虑每次窗口之内的黑色格子数来看缺失多少
'''
