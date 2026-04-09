class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = sum(cardPoints)
        if k == len(cardPoints) :
            return res
        cur = 0
        for right, val in enumerate(cardPoints) :
            cur += val
            left = right + k - len(cardPoints) + 1
            if left < 0 :
                continue
            res = min(res, cur)
            cur -= cardPoints[left]
        return sum(cardPoints) - res

'''
解析；
定长滑动窗口，使用逆向思维
只需计算长为 n-k 的窗口的和的最小值即可
然而时间复杂度为on

而参考灵神题解：
方法二：正向思维
答案等于如下结果的最大值：
前 k 个数的和。
前 k−1 个数以及后 1 个数的和。
前 k−2 个数以及后 2 个数的和。
……
前 2 个数以及后 k−2 个数的和。
前 1 个数以及后 k−1 个数的和。
后 k 个数的和。
算法
计算前 k 个数的和，记作 s。初始化答案 ans=s。
从 i=1 开始枚举到 i=k。
每次枚举，把 s 增加 cardPoints[n−i]−cardPoints[k−i]，然后更新 ans 的最大值。
返回 ans。

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = s = sum(cardPoints[:k])
        for i in range(1, k + 1):
            s += cardPoints[-i] - cardPoints[k - i]
            ans = max(ans, s)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/solutions/2551432/liang-chong-fang-fa-ni-xiang-si-wei-zhen-e3gb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

时间复杂度为ok
'''
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
